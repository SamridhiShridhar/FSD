import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def current_date_time(request):
    dt=datetime.datetime.now()
    resp="<h1>Current date and time is %s</h1>" %(dt)
    return HttpResponse(resp)

def table_of_squares(request,s,e):
    resp=""

    for i in range(1,e+1):
        resp+="<p> %d * %d = %d </p>"%(s,i,s*i)
    return HttpResponse(resp)

def vowel_consonants(request,sentence):
    vowel_cnt=0
    consonant_cnt=0
    vowel_dict=dict()
    consonant_dict=dict()
    for char in sentence:
        if char.isalpha():
            if char in "aeiouAEIOU":
                vowel_cnt+=1
                vowel_dict[char]=vowel_dict.get(char,0)+1
            else:
                consonant_cnt+=1
                consonant_dict[char]=consonant_dict.get(char,0)+1
    resp="<h1> no. of vowels: %d and no. of consonants: %d </h1>"%(vowel_cnt,consonant_cnt)
    resp+="<h2>vowel counter</h2>"
    for key,value in vowel_dict.items():
        resp+="<p>%s occurs %d times </p>" %(key,value)
    resp+="<h2>consonant counter</h2>"
    for key,value in consonant_dict.items():
        resp+="<p>%s occurs %d times </p>" %(key,value)
    return HttpResponse(resp)

def find_mode(request, listofnum):
    arr=listofnum.split(",")
    num_count=dict()
    for num in arr:
        num_count[num]=num_count.get(num,0)+1
    num_count=sorted(num_count.items(),key=lambda i:i[1])
    num_count.reverse()
    resp="<span style=color:red>%s</span> appears <span style=background-color:yellow>%s</span> times" %(num_count[0][0],num_count[0][1])
    return HttpResponse(resp)

def vote(request,age):
    if age<60:
        x=60-age
        resp="You cannot avail Vote from Home as you are %d years younger than the threshold age " %(x)
    else:
        x=age-60
        resp="You are eligible for Vote from Home as you exceeded %d years than the threshold age" %(x)
    return HttpResponse(resp)

def n_hours(request, n):
    dt=datetime.datetime.now()+datetime.timedelta(hours=n)
    resp="<h1>date and time is %s </h1>" %(dt)
    return HttpResponse(resp)