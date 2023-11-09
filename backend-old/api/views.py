
from django.shortcuts import render
from rest_framework.response import Response
import openai
from rest_framework.decorators import api_view
from .utils import get_pages 
import os
from dotenv import load_dotenv


# from rest_framework.response import StreamingHttpResponse
from django.http import StreamingHttpResponse
from rest_framework.views import APIView
from io import StringIO


load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

@api_view(['POST'])
def get_post(request, MaxToken=50, outputs=3):
    text = request.data["content"]
    response = StreamingHttpResponse(
        get_pages(text),
        status=200,
        content_type="text/csv",
    )
    response["Content-Disposition"] = 'attachment; filename="reports.csv"'
    return response


    # text=request.data["content"]
    # if request.method == 'POST':
    #     result = get_pages(text)
    #     return Response(result)
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


