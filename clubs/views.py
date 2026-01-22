# clubs/views.py
# Handles web requests for the clubs app.
# Includes listing clubs, adding new clubs, and deleting clubs.


from django.shortcuts import render, redirect
from .forms import ClubForm
from .models import Club
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout



def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # saves the user to the database
            login(request, user)  # logs in the user immediately
            messages.success(request, "Account created successfully!")
            return redirect("club_list")  # redirect after login
    else:
        form = RegisterForm()
    
    return render(request, "clubs/register.html", {"form": form})

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "clubs/register.html", {"form": form})  # <-- use register.html


def login_view(request):
    if request.user.is_authenticated:
        return redirect("club_list")  # already logged in

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("club_list")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "clubs/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def add_club(request):
    if request.method == "POST":
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("club_list")
    else:
        form = ClubForm()

    return render(request, "clubs/add_club.html", {"form": form})




def club_list(request):
    clubs = Club.objects.all()
    return render(request, 'clubs/club_list.html', {'clubs': clubs})

@login_required
def delete_club(request, club_id):
    club = Club.objects.get(id=club_id)
    club.delete()
    return redirect("club_list")


def home_view(request):
    login_error = None
    signup_form = UserCreationForm()

    if request.method == "POST":
        if "login_submit" in request.POST:
            # LOGIN form submitted
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("club_list")
            else:
                login_error = "Invalid username or password."

        elif "signup_submit" in request.POST:
            # SIGNUP form submitted
            signup_form = UserCreationForm(request.POST)
            if signup_form.is_valid():
                user = signup_form.save()
                login(request, user)
                return redirect("club_list")

    return render(
        request,
        "clubs/home.html",
        {"login_error": login_error, "signup_form": signup_form},
    )