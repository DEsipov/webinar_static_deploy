from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import cache_page
from django.conf import settings

from .forms import PostForm
from .models import Post

User = get_user_model()


def get_paginator(request, post):
    paginator = Paginator(post, settings.NUMBER_POST)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)


def home(request):
    context = {
        'name': 'Джон Доу',
    }
    return render(request, 'posts/home.html', context)


def index(request):
    post_list = Post.objects.all()
    page_obj = get_paginator(request, post_list)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


@login_required
def post_create(request):
    form = PostForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('posts:index')
    context = {
        'form': form,
        'is_edit': False
    }
    return render(request, 'posts/create_post.html', context)
