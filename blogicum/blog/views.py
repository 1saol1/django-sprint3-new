from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post, Category


AMOUNT_OF_POSTS = 5


def get_published_posts():
    return Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )


def index(request):
    template = 'blog/index.html'

    posts = get_published_posts()[:AMOUNT_OF_POSTS]
    context = {'posts': posts}
    return render(request, template, context)


def post_detail(request, id):
    post = get_object_or_404(
        Post,
        id=id,
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True)

    template = 'blog/detail.html'
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True)
    
    posts = get_published_posts().filter(category=category)
    context = {'category': category, 'posts': posts}
    return render(request, template, context)
