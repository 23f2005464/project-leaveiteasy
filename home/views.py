from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"landing_page.html")

def notfound_page(request):
    return render(request,"404.html")
    