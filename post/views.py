from django.shortcuts import render
from django.http import HttpResponse
from post.models import Post

def post_view(request):
    posts = Post.objects.all()
    return render(request=request, template_name='post_list.html')
    

def main_page(request):
    return render(request, template_name="index.html")

