
#coding=utf-8
from django.http import HttpResponse


def goods_view(request):
    return HttpResponse('hello goods!')


def user_views(request):
    return HttpResponse('用户登录功能')

