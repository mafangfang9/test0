
#coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render


def goods_view(request):
    return HttpResponse('hello goods!')


def user_view(request):
    return HttpResponse('用户登录功能')


def article_view(request):
    return render(request,'article.html')