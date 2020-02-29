from django.shortcuts import render
posts = [
    {
        "author": "vishnu",
        "title": "Blog Post 1",
        "content": "first post content",
        "date": "20-Feb-2020"
    },
    {
        "author": "pradeep",
        "title": "Blog Post 2",
        "content": "second post content",
        "date": "21-Feb-2020"
    }
]

def home(request):
    context = {
        "posts": posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {"title":"About"})
