from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to PantherConnect!")

def about(request):
    return HttpResponse("PantherConnect helps connect campus clubs!")
