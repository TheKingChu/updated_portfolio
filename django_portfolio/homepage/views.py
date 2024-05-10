from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "homepage/index.html")

def agodsdraw(request):
    return render(request, "homepage/agodsdraw.html")

def negativeeffect(request):
    return render(request, "homepage/negativeeffect.html")