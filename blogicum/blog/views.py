from django.shortcuts import render, get_object_or_404

from blog.models import Category, Post
from blog.constants import AMOUNT_OF_POSTS
from blog.service import get_published_posts


def index(request):
    template = 'blog/index.html'

    posts = get_published_posts()[:AMOUNT_OF_POSTS]
    context = {'posts': posts}
    return render(request, template, context)


def post_detail(request, post_id):
    post = get_object_or_404(
        get_published_posts(),
        id=post_id)

    template = 'blog/detail.html'
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True)

    posts = get_published_posts(category.posts)
    context = {'category': category, 'posts': posts}
    return render(request, template, context)
