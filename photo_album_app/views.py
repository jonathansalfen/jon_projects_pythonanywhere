from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm


# photo app

def about(request):
    return render(request, 'old_site/about.html')

def old_index(request):
    return render(request, 'old_site/old_index.html')

def portfolio(request):
    return render(request, 'old_site/portfolio.html')

def contact(request):
    return render(request, 'old_site/contact.html')
