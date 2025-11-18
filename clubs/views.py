from django.shortcuts import render, redirect
from .forms import ClubForm
from .models import Club


def add_club(request):
    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('club_list')  # Redirect to a list of clubs
    else:
        form = ClubForm()
    return render(request, 'clubs/add_club.html', {'form': form})

def club_list(request):
    clubs = Club.objects.all()
    return render(request, 'clubs/club_list.html', {'clubs': clubs})
