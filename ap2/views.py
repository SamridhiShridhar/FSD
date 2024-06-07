import datetime
from django.shortcuts import render
from django.template import Context, Template, loader
from django.http import HttpResponse
#create your views here

def members(request):
    template=loader.get_template('template.html')
    context = {
        'myname':'Samridhi'
    }
    return HttpResponse(template.render(context,request))

def testing(request):
    template= loader.get_template('template1.html')
    context = {
        'greeting':1,
    }
    return HttpResponse(template.render(context,request))

def testing1(request):
    template = loader.get_template('template2.html')
    context = {
        'fruits' : ['Apple','Banana','Cherry','Mango','Watermelon']
    }
    return HttpResponse(template.render(context, request))

def testing2(request):
    template=loader.get_template('template3.html')
    return HttpResponse(template.render())

def showlist(request):
    fruits=["Mango","Apple","Banana","Jackfruits"]
    student_names=["Tony","Mony","Sony","Bob"]
    return render(request,'showlist.html',{"fruits":fruits,"student_name":student_names})

def home(request):
    return render(request,'home.html')
def aboutus(request):
    return render(request,'aboutus.html')
def contactus(request):
    return render(request,'contactus.html')

def getpos(request):
    return render(request,'ap2/pos.html')

def stable(request):
    return render(request, 'stable.html')