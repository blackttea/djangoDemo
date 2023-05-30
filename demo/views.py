from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def index(body):
    return HttpResponse(json.dumps({
        'code': 200,  # code由前后端配合指定
        'message': "hello-world",  # 提示信息
        'data': "hello-world",  # 返回单个对象
    }, ensure_ascii=False), 'application/json')
