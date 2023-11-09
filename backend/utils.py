from openai import OpenAI
import json
from duckduckgo_search import DDGS
from flask import jsonify
import requests
from bs4 import BeautifulSoup
from os import getenv

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = getenv("KEY")
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

def _from_one(question: str) -> dict:
    pages = _get_pages(question)
    answer = {
        "question": question,
        "pages": pages
    }

    return answer


def get_pages_content(pages: dict):
    content = ""
    for page in pages.get("pages"):
        try:
            page_response = requests.get(page.get("link")).text
            soup = BeautifulSoup(page_response)
            page_content = soup.text

            content += summarize_page_content(page_content, pages.get("question"))

        except:
            print("Проблемы с сайтом")

    return content


def summarize_content(data: str):
    content_size = 0
    is_processed = True
    str_answer = ""

    if (len(data) < 8000):
        content_size = len(data)

    else:
        content_size = 8000

    prompt = "Обработай текст, указанный далее. Твоя задача переписать текст и не потерять данные. Текст может содержать повторения, в таком случае оставь уникальный контент. Ответ должен быть обьемным и не коротким" + data[:content_size]

    while is_processed:
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

        try:
            for part in ai_answer:
                if part.choices[0].delta.content is None:
                    continue

                str_answer += part.choices[0].delta.content

            is_processed = False

        except IndexError:
            print("Ответ не получен")
            continue

    return str_answer


def summarize_page_content(data: str, question: str):
    is_processed = True
    str_answer = ""

    prompt = f"Задача: Анализ контента сайта с артефактами Контент сайта: {data[:7000]}. Шаги: 1. Игнорировать любые артефакты, ошибки или ненужную информацию. 2. Извлечь основные данные из контента. 3. Учитывать все важные детали при анализе. Вопрос: {question}"

    while is_processed:
        ai_answer = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
            stream=True,
            timeout=20
        )

        try:
            for part in ai_answer:
                if part.choices[0].delta.content is None:
                    continue

                str_answer += part.choices[0].delta.content

            is_processed = False

        except IndexError:
            print("Ответ не получен")
            continue

    return str_answer


def get_pages(app, object: str) -> list:
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
        pages = _from_one(answer.get("title"))
        pages["id"] = answer.get("id")

        with app.app_context():
            yield jsonify(pages).get_data(as_text=True)


def generate_answer(question: dict):
    pages_content = get_pages_content(question)

    question["content"] = summarize_content(pages_content)
    return question

    # question["content"] = "None"
