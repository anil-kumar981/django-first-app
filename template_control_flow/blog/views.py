from django.shortcuts import render

# Create your views here.
def blog_home(request):
    context = {
        "name": "John Doe",
        "author":"",
        "html_content": "<p>This is a <strong>blog post</strong> with HTML content.</p>",
        "age": 30,
        "hobbies": ["Reading", "Traveling", "Cooking"],
        "is_active": True,
    }
    return render(request, 'blog_home.html', context)