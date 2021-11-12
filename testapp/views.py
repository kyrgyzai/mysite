from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def index(request, question_id):
    return HttpResponse("Index")

def detail(request):
    return HttpResponse("Detail")

def info(request):
    return HttpResponse("Info")