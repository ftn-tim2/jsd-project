from _datetime import datetime
from datetime import timezone, timedelta
import json
import re

from django.contrib import messages
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

def report_week(request):
    return 1
    
def report_city(request):
    return 1

def do_nothing(request):
    return HttpResponse('')