from django.shortcuts import render
from django.http import HttpResponse
import requests
import json


# Create your views here.
def table(request):
    userData = {
        "year": "42",
        "term": "2",
        "username": "320220941801",
        "userpassword": "Lkjhgfdsa114514"
    }
    table0 = requests.post(url='https://cyonline.lzu.edu.cn/server/common_apis/get_kechengbiao?', data=userData).json()
    print(table0)
    print(type(table0))
    for i in range(0, len(table0['kechengbiao'])):
        for j in range(0, len(table0['kechengbiao'][i]['time'][0]['week'])):
            print(table0['kechengbiao'][i]['time'][0]['week'][j])
    return HttpResponse(json.dumps(table0))
