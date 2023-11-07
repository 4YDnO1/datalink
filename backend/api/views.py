
from django.shortcuts import render
from rest_framework.response import Response
import openai
from rest_framework.decorators import api_view
from .utils import get_pages 
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

@api_view(['POST'])
def get_post(request, MaxToken=50, outputs=3):
    # print(request.data)
    text='Биология'
    if request.method == 'POST':
        result = get_pages(text)
        return Response(result)
    
        # response = openai.completions.create(
        #     model="gpt-3.5-turbo-instruct",
        #     prompt=text,
        #     max_tokens=100,
        #     temperature=0.7,
        #     n=1,
        #     stop=None,
        #     stream = False
        # )

        # output = list() 

        # for k in response.choices: 
        #     output.append(k.text.strip()) 
        # print(output)
        # txt2 = ''.join(output)

        # return Response(txt2)
