from django.shortcuts import render

# Create your views here.
def blog_Details(request):
    post = {
        'title': 'My First Blog Post',
        'content': 'This is the content of my first blog post.',
        'author': 'John Doe',
        'published_date': '2024-06-01',
    }
    return render(request, 'blog_details.html', {'post': post})