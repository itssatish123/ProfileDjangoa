
from ast import Pass
from math import e
from operator import length_hint
from sys import exception
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from education.models import education
from news.models import news
from enqData.models import EnqData
from django.core.mail import send_mail

def header(request):
    
    return render(request,"header.html")

def footer(request):
    
    return render(request,'footer.html')

def index(request):
    
    return render(request,"index.html")

def about(request):
        newsData = news.objects.all()
        EducationData = education.objects.all()
       
        data = {
            'educationData':EducationData,
            'newsData':newsData

        }
        return render(request,'about.html',data)
 

   
def contact(request):
    
   if request.method == 'POST':
    data= {}

   try:
    name = request.POST.get('name')
    email = request.POST.get('email')
    message =request.POST.get('message')
    en = EnqData(nameFirst=name,mail=email,messageData=message)
    en.save()
    data= {
       'name': name,
       'email': email,
       'message' : message,
       
    }
 

    return render(request,'contact.html',data)

   except :
          print("error")
          return render(request,'contact.html',data)

   

def portfolio(request): 

    return render(request,'portfolio.html')

def formdata(request):

    return HttpResponse("this is data")

def thankyou(request):
   if request.method == 'POST':
    data= {}
   try:
    name = request.POST.get('name')
    email = request.POST.get('email')
    message =request.POST.get('message')
  
    
    data= {
       'name': name,
       'email': email,
       'message' : message,
       
    }

   
    return render(request,'thankYou.html',data)

   except :
          print("error")
          return render(request,'thankYou.html',data)
