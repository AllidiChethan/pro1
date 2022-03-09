from django.http import HttpResponse


def home(request):
    return HttpResponse("welcome to chetana web page")

def allidi(request):
    return HttpResponse("surname")

def