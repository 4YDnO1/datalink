from openai import OpenAI
import json
from duckduckgo_search import DDGS
import os
from dotenv import load_dotenv
from django.conf import settings
import pika
import time
import json

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(
    api_key=OPENAI_API_KEY
)


def _get_pages(question: str) -> list:
    scoped_answer: list[dict] = []

    with DDGS() as ddgs:
        results = [r for r in ddgs.text(question, max_results=5)]
        for result in results:
            scoped_answer.append({
                "title": result.get("title"),
                "link": result.get("href")
            })

    return scoped_answer

def _from_one(question: str) -> object:
    pages = _get_pages(question)
    answer = {
        "question": question,
        "pages": pages
    }

    return answer


def get_pages(object: str) -> list:
    prompt_format = """Ответь в формате JSON: [{"id": <id>, "title": <title>}]"""
    prompt = f"Напиши 10 вопросов на тему {object}." + prompt_format

    ai_answer = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
        stream=True
    )

    str_answer = ""

    for part in ai_answer:
        if part.choices[0].delta.content is None:
            continue

        str_answer += part.choices[0].delta.content

    json_answer = json.loads(str_answer)

    for answer in json_answer:
        pages = _from_one(answer['title'])
        pages['id'] = answer.get("id")
        json_info = json.dumps(pages, ensure_ascii=False)
        # print(pages)
        # print(json_info)
        yield json_info



def connect(queues = ["to_resize", "to_socket"], retry = True):
    connected = False
    while connected == False:
        try:
            credentials = pika.PlainCredentials(username=settings.RMQ_USER,
                password=settings.RMQ_PASS)
            parameters = pika.ConnectionParameters(host=settings.RMQ_HOST,
                port=settings.RMQ_PORT, credentials=credentials)
            connection = pika.BlockingConnection(parameters=parameters)
            channel = connection.channel()
            for queue in queues:
                channel.queue_declare(queue = queue)
            connected = True
            return connection, channel
        except:
            pass
        if retry == False: return None, None
        time.sleep(5)