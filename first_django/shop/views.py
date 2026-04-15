from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the shop index.")

def products(request):
    return HttpResponse("These are our products.")