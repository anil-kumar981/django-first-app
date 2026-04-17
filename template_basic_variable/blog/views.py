
from django.shortcuts import render

# Create your views here.
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def blog_home(request):
    context = {
        'name': 'John Doe',
        'age': 30,
        'user': User('Alice', 25),
        'numbers': [1, 2, 3, 4, 5],
        'is_authenticated': True,
    }
    return render(request, 'blog_home.html', context)