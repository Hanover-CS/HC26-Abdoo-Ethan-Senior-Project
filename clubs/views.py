# clubs/views.py
# Handles web requests for the clubs app.
# Includes listing clubs, adding new clubs, and deleting clubs.


from django.shortcuts import render, redirect
from .forms import ClubForm
from .models import Club
from django.contrib import messages



from django.shortcuts import render, redirect


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


def delete_club(request, club_id):
    club = Club.objects.get(id=club_id)
    club.delete()
    return redirect("club_list")

def home(request):
    return render(request, "home.html")