#coding=utf-8
from django.http import HttpResponse


def goods_view(request):
    return HttpResponse('hello goods!')

def sss_view(request):
    return HttpResponse("123")