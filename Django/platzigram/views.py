# -*- coding:utf-8 -*-

from django.http import HttpResponse
import json

def hello_world(request):
    return HttpResponse( 'Hello world!' )


def sort_integers(request): 
    number = sorted( list(map(lambda x: int(x), request.GET['numbers'].split(","))) ) 
    data = {
        "status":"ok", 
        "numbers": number, 
        "message": "Integer sorted successfuly"
    }
    return HttpResponse( json.dumps(data), content_type='application/json' )


def say_hi(request, name, age):
    
    if age< 12: 
        message = "Sorry {}, you are not allowed here".format(name)
    else: 
        message = "Hello, {}! Welcome to Platzigram".format(name)
    
    return HttpResponse(message)