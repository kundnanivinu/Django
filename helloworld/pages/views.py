# pages/views.py

from django.shortcuts import render
from django.http import HttpResponse


def homePageView(request):
    return HttpResponse('Hello World, Vinu!')

#Basically we’re saying whenever the view function homePageView is called, return the text “Hello, World!”. More specifically, we’ve imported the built-in HttpResponse method so we can return a response object to the user. Our function homePageView accepts the request object and returns a response with the string Hello, World!.