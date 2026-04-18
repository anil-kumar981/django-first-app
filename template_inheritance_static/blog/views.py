from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def submit_post(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        hobbies = request.POST.get('hobbies')

        # Here you would typically save the post to the database
        return render(request, 'submit.html', {'name': name, 'age': age, 'hobbies': hobbies})
    return render(request, 'submit.html')