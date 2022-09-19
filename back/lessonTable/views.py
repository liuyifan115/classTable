from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import time
from datetime import datetime
from . import admin
import random
import ast


def getweek():
    return int(time.strftime("%W")) - 34


def getday():
    return datetime.now().isoweekday() - 1


# Create your views here.
def table(request):
    userData = json.loads(request.body)
    data = {
        'year': '42',
        'term': '2',
        'userpassword': userData['userpassword'],
        'username': userData['username'],
    }
    table0 = requests.post(url='https://cyonline.lzu.edu.cn/server/common_apis/get_kechengbiao?', data=data).json()
    print(getweek())
    print(getday())
    list = []
    list1 = []
    for i in range(0, len(table0['kechengbiao'])):
        for j in range(0, len(table0['kechengbiao'][i]['time'])):
            for k in range(0, len(table0['kechengbiao'][i]['time'][j]['week'])):
                if table0['kechengbiao'][i]['time'][j]['week'][k] == getweek() and table0['kechengbiao'][i]['time'][j]['day'] == getday():
                    lessonToday = table0['kechengbiao'][i]['time'][j]['juti'][1]
                    list.append(lessonToday)
    try:
        userNew = admin.models.user.objects.get(username=userData['username'])
        admin.models.user.objects.filter(username=userData['username']).update(juti=list)
    except:
        userNew = admin.models.user(username=userData['username'], password=userData['userpassword'], juti=list)
        userNew.save()
    finally:
        for i in list:
            list1.append(i + 1)
        list += list1
        list.sort()
        list = [str(i) for i in list]
        table = ', '.join(list)
        ans = {
            'status_code': 114514,
            'ans': 'success',
            'table': table
        }
        print(list)
        print(table)
        return HttpResponse(json.dumps(ans))


def creatteam(request):
    teamID = str(random.randint(10000000, 99999999))
    data = json.loads(request.body)
    username = data.get('username')
    teamName = data.get('teamname')
    if admin.models.user.objects.get(username=username).jointeam == '-1':
        try:
            teamNew = admin.models.team.objects.get(teamname=teamName)
            ans = {
                'status_code': -114514,
                'ans': '团队名称已存在',
            }
            return HttpResponse(json.dumps(ans))
        except Exception as e:
            teamNew = admin.models.team(teamname=teamName, teamid=teamID)
            admin.models.user.objects.filter(username=username).update(jointeam=teamID)
            teamNew.save()
            member = ast.literal_eval(admin.models.team.objects.get(teamid=teamID).member)
            member.append(username)
            admin.models.team.objects.filter(teamid=teamID).update(member=member)
            ans = {
                'status_code': 200,
                'ans': '创建成功',
                'teamid': teamID,
                'teamname': teamName,
            }
            return HttpResponse(json.dumps(ans))
    else:
        ans = {
            'status_code': -1,
            'ans': '你已经有一个团队了',
        }
        return HttpResponse(json.dumps(ans))


def jointeam(request):
    data = json.loads(request.body)
    teamID = data.get('teamid')
    username = data.get('username')
    try:
        for i in ast.literal_eval(admin.models.team.objects.get(teamid=teamID).member):
            if i == username:
                ans = {
                    'status_code': -114514,
                    'ans': '你已经在团队里了',
                }
                return HttpResponse(json.dumps(ans))
            else:
                member = ast.literal_eval(admin.models.team.objects.get(teamid=teamID).member)
                print(member)
                member.append(username)
                admin.models.team.objects.filter(teamid=teamID).update(member=member)
                ans = {
                    'status_code': 114514,
                    'ans': '加入成功',
                    'teamname': admin.models.team.objects.get(teamid=teamID).teamname
                }
                return HttpResponse(json.dumps(ans))
    except:
        ans = {
            'status_code': -114,
            'ans': '团队不存在',
        }
        return HttpResponse(json.dumps(ans))

def teamtable(request):
    list1 = []
    data = json.loads(request.body)
    teamID = data.get('teamid')
    team = admin.models.team.objects.get(teamid=teamID)
    juti = []
    member = ast.literal_eval(team.member)
    for i in range(0, len(member)):
        user = admin.models.user.objects.get(username=member[i])
        juti += ast.literal_eval(user.juti)
    juti = list(set(juti))
    for i in juti:
        list1.append(i + 1)
    juti += list1
    juti.sort()
    admin.models.team.objects.filter(teamid=teamID).update(table=juti)
    juti = [str(i) for i in juti]
    table = ', '.join(juti)
    ans = {
        'status_code': 114514,
        'ans': 'success',
        'juti': table
    }
    return HttpResponse(json.dumps(ans))
