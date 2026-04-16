from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world. You're at the blog index.")
def post_details(request, id):
    return HttpResponse(f"Post id is {id}")

def username_details(request, username):
    return HttpResponse(f"Username is {username}")

def article_details(request, year):
    return HttpResponse(f"Article year is {year}")

def article_year_month(request, **krargs):
    return HttpResponse(f"Article year is {krargs['year']} and month is {krargs['month']}")