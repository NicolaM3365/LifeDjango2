from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


posts = [
    {
        'author': 'Steve K',
        'blog_title': 'First Blog Post',
        'content': 'Content for the first post.',
        'date_posted': '12/07/2023'
    },

     {
        'author': 'Scott K',
        'blog_title': 'Second Blog Post',
        'content': 'Content for the second post.',
        'date_posted': '13/07/2023'
    }
]


# def home(request):
#     return HttpResponse('<h1>Life Blog Home</h1>')


def home(request):
     context = {
        'posts': posts
    }
     return render(request, 'life_blog/home.html', context)


def about(request):
    return render(request, 'life_blog/about.html', {'title': 'About'})
