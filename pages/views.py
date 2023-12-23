from django.shortcuts import render
from django.http import HttpResponse


def homePageView():
    return HttpResponse('Hello World from Django!')
