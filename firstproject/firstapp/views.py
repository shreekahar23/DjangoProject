# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):

    my_dict={'insert_me': "Hello I am inside the insert_tag with function index also I am available in view.py \n"}
   # return render(request, 'index.html', context=my_dict)
    return render(request, 'index1.html', context=my_dict)


#def index(request):
 #   return HttpResponse("HEllo to the second day")

#def second(request):
 #   return HttpResponse("Hi, My name is Shreya")