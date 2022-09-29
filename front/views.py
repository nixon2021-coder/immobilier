from datetime import date
from email import message
import email
from tokenize import Name
from unicodedata import name
from django.http import request
from django.shortcuts import render
from front.models import *


def home(request):
    #boo = True
    #print(boo)
    return render(request , "front/pages/index.html",  locals())


   
     


def about(request):
    #boo = True
    #print(boo)
    return render(request , "front/pages/about.html" , locals())

def contact(request):
    
    if request.method == "POST" : 

        nom = request.POST.get('nom')
        Prenom = request.POST.get('prenom')
        Prix = request.POST.get('prix')
        Numero = request.POST.get('numero')
        Date = request.POST.get('date')
        Message = request.POST.get('message')
        Email = request.POST.get('email')

        #send_mail(
             #nom,
             #Prenom,
             #Prix,
             #Numero,
             #Date,
             #Message,
             #Email,
             #['nixondago9@gmail.com']

        #)


        Contact.objects.create(
            nom=nom,
            prenom=Prenom,
            prix=Prix,
            numero=Numero,
            date=Date,
            Message=Message,
            email=Email,)

        return render(request, 'front/pages/index.html',locals(),)
        


    return render(request , "front/pages/contact.html" , locals())
    

def gallery(request):
    return render(request , "front/pages/gallery.html" , locals())

def properties(request):
    return render(request , "front/pages/properties.html" , locals())
