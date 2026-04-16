from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "shop_home.html")

def about(request):
    return render(request, "shop_about.html")