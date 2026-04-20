from django.shortcuts import render

# Create your views here.
def home(request):
    students = [
        {'name': 'Alice', 'age': 20, "class": "A"},
        {'name': 'Bob', 'age': 22, "class": "B"},
        {'name': 'Charlie', 'age': 21, "class": "C"},
    ]
    return render(request, 'home.html', {'students': students})