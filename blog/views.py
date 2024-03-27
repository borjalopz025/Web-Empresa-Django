from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.
def blog(req):

    post = Post.objects.all()

    return render(req, 'blog/blog.html', {'post': post})


def category(req, category_id):

    category = get_object_or_404(Category, id=category_id)
    return render(req, "blog/category.html", {'category': category})