
# coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse
import json
from collections import OrderedDict
from django.views.decorators.csrf import csrf_exempt
import MySQLdb
from django.db.models import Q
import sys
sys.path.append('E:\python\Scripts\guest\sign')
from sign.models import users
# import models

# Create your views here.
def  select(db,passwd,table_name):
    db = MySQLdb.connect(host='localhost', user='root', passwd='', db='test', port=3306)
    cursor = db.cursor()
    sql = "SELECT * FROM name_test WHERE"
    return sql

@csrf_exempt
def login(request):
    # db = MySQLdb.connect(host='localhost', user='root', passwd='', db='test', port=3306)
    # cursor = db.cursor()
    request.method == 'POST'
    username = request.POST.get('username')
    password = request.POST.get('password')
    # sql = "SELECT * FROM name_test WHERE username = " + "'" + username + "'" + "AND Tel = " + "'" + password + "'"
    # print sql
    # if cursor.execute(sql) != 0:
    #     data = OrderedDict()
    #     data["error"] = 0
    #     data["message"] = u"登录成功"
    #     # data["data"] = {
    #     #     "locate": {
    #     #         "code": "441900",
    #     #         "name": "东莞",
    #     #         "dp_id": "219"
    #     #     }}
    #     d1 = json.dumps(data)
    #     return HttpResponse(d1)
    # else:
    #     data = OrderedDict()
    #     data["error"] = 1
    #     data["message"] = u"用户名或密码不正确"
    #     d1 = json.dumps(data)
    #     return HttpResponse(d1)
    # db = models.users
    if len(username) <= 30 and len(password) <= 11 and isinstance(password,(int)) == True:
        if users.objects.filter(name="") or users.objects.filter(password=""):
            data = OrderedDict()
            data["error"] = 1
            data["message"] = u"必填项为空"
            d1 = json.dumps(data)
            return JsonResponse(data)
        if users.objects.get(name=username) and user.objects.get(password=password):
            data = OrderedDict()
            data["error"] = 0
            data["message"] = u"登录成功"
            d1 = json.dumps(data)
            return JsonResponse(data)
        else:
            data = OrderedDict()
            data["error"] = 1
            data["message"] = u"账号或密码错误"
            d1 = json.dumps(data)
            return JsonResponse(data)
    else:
        if len(username) > 30:
            data = OrderedDict()
            data["error"] = 1
            data["message"] = u"用户名长度错误"
            return JsonResponse(data)
        if len(password) > 11:
            data = OrderedDict()
            data["error"] = 1
            data["message"] = u"密码长度错误"
            return JsonResponse(data)
        if isinstance(password,(int)) == False:
            data = OrderedDict()
            data["error"] = 1
            data["message"] = u"密码格式错误"
            return JsonResponse(data)





@csrf_exempt
def signup(request):
    # db = MySQLdb.connect(host='localhost', user='root', passwd='', db='test', port=3306)
    # cursor = db.cursor()
    request.method == 'POST'
    username = request.POST.get('username')
    password = request.POST.get('password')
    # sql = "SELECT * FROM name_test WHERE username = " + "'" + username + "'"
    # if cursor.execute(sql) != 0:
    #     data = OrderedDict()
    #     data["error"] = 1
    #     data["message"] = u"用户名已经存在！"
    #     d1 = json.dumps(data)
    #     return HttpResponse(d1)
    # else:
    #     sql1 = "SELECT * FROM name_test"
    #     id = cursor.execute(sql1) + 1
    #     print id
    #     key = (str(id), str(username), "50", "M", str(password))
    #     sql = "INSERT INTO name_test VALUES" + str(key)
    #     cursor.execute(sql)
    #     data = OrderedDict()
    #     data["error"] = 0
    #     data["message"] = u"注册成功！"
    if len(username) <= 30 and len(password) <= 11:
        try:
            users.objects.get(name=username)
            data = OrderedDict()
            data["error"] = 1
            data["message"] = u"用户名已经存在！"
            return JsonResponse(data)
        except:
            users.objects.create(name=username,password=password)
            data = OrderedDict()
            data["error"] = 1
            data["message"] = u"注册成功！"
            return JsonResponse(data)

    else:
        data = OrderedDict()
        data["error"] = 1
        data["message"] = u"用户名格式错误"
        return JsonResponse(data)

