from openai import OpenAI
import json
from duckduckgo_search import DDGS

client = OpenAI(
    api_key="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"
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


def get_pages(object: str):
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
    answer_list = []

    for answer in json_answer:
        pages = _from_one(answer['title'])
        answer_list.append(pages)

    return answer_list