import email
import requests
from multiprocessing import context
from urllib import request
from django.shortcuts import render
from django.contrib import messages

from Dental.models import About, Categories, Blog

def send_msg(text1):
    token = "1907297658:AAF6PFeOWh8Fd7oRCrjcfkOCEx6GETUFHZM"
    chat_id = "678056623"

    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text1
    
    results = requests.get(url_req)

def bookingnow(request):
    if request.method == "POST":
        name = "NAME: " + request.POST['your-name']
        phone = "\nPHONE: " + request.POST['your-phone']
        email =  "\nE-MAIL: " + request.POST['your-email']
        address = "\nADDRESS: " + request.POST['your-address']
        schedule = "\nSCHEDULE: " + request.POST['your-scheldule']
        time = "\nTIME: " + request.POST['your-time']
        message = "\nMESSAGE: " + request.POST['your-message']
        texts = name + phone + email + address + schedule + time + message
        send_msg(texts)
        messages.success(request, 'Appointment sending successful')
    return render(request, 'bookingnow.html', {})

def home(request):
    return render(request, 'home.html', {})

def about(request):
    about = About.objects.all()
    context = {'about': about}
    return render(request, 'about.html', context)

def service(request):
    return render(request, 'service.html', {})

def pricing(request):
    return render(request, 'pricing.html', {})

def blog(request):
    categories = Categories.objects.all()
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
        'categories': categories
        }
    return render(request, 'blog.html', context)

def contact(request):
    return render(request, 'contact.html', {})

def blogdetails(request):
    return render(request, 'blog-details.html', {})