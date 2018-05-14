# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
  context = {
  "time": strftime("%b %d, %Y %H:%M %p", gmtime())
  }
  return render(request,'timesdisplay/index.html', context)