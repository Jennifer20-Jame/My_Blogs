from django.shortcuts import render
from .models import Post 

def home(request):
     """Return the list of blogposts"""
     Blogs = Post.objects.all()
     context = {'posts': Blogs}
     return render(request, template_name='blogs/home.html', context=context)
    
