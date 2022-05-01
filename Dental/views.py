from multiprocessing import context
from urllib import request
from django.shortcuts import render

from Dental.models import About, Categories, Blog

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