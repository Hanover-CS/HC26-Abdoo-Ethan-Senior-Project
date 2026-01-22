from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Welcome to PantherConnect!")

def about(request):
    return HttpResponse("PantherConnect helps connect campus clubs!")

def contact(request):
    return HttpResponse("Contact page for PantherConnect!")

def login_view(request):
    return render(request, 'clubs/login.html')