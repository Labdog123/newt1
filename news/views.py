from django.shortcuts import render, redirect,get_object_or_404
from .forms import CreateUserForm, login_form, CreatePostForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.paginator import Paginator
from .decorators import unauthenticated_user

@unauthenticated_user
def user_login(request):
    form = login_form()
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd["password"])

            if user is not None:
                login(request, user)
                messages.success(request, 'Login was successful')
                return redirect('/')

            else:
                messages.info(request, 'Username or Password in incorrect')

        else:
            messages.info(request, 'Enter Valid Input')
    else:
        context = {'form': form}
        return render(request, 'news/login.html', context)

@unauthenticated_user
def create_user(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account Successfully Created' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'news/register.html', context)

def user_logout(request):
    logout(request)
    return redirect('/')

def news_list(request):
    post = Post.objects.all().order_by('-date_published')
    paginator = Paginator(post, 3)
    page = request.GET.get('page')
    post = paginator.get_page(page)

    context = {'post': post}
    return render(request, 'news/news_list.html', context)

def news_detail(request, pk):
    post_detail = get_object_or_404(Post, id=pk)
    context = {'post_detail': post_detail}
    return render(request, 'news/news_detail.html', context)
# Create your views here.

@login_required(login_url='login')
def create_new_post(request):
    form = CreatePostForm()
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        form.save()

        return redirect('/')

    context = {'form': form}
    return render(request, 'news/create_new_post.html', context)

def international_page(request):
    post = Post.objects.filter(category__iexact="international")
    context = {'post': post}
    return render(request, 'news/category/international.html', context)


def fashion_page(request):
    post = Post.objects.filter(category__iexact="fashion")
    context = {'post': post}
    return render(request, 'news/category/fashion.html', context)


def agriculture_page(request):
    post = Post.objects.filter(category__iexact="agriculture")
    context = {'post': post}
    return render(request, 'news/category/agriculture.html', context)


def finance_page(request):
    post = Post.objects.filter(category__iexact="finance")
    context = {'post': post}
    return render(request, 'news/category/finance.html', context)


def health_page(request):
    post = Post.objects.filter(category__iexact="health")
    context = {'post': post}
    return render(request, 'news/category/health.html', context)


def local_page(request):
    post = Post.objects.filter(category__iexact="local")
    context = {'post': post}
    return render(request, 'news/category/local.html', context)


def oil_page(request):
    post = Post.objects.filter(category__iexact="oil")
    context = {'post': post}
    return render(request, 'news/category/oil.html', context)


def politics_page(request):
    post = Post.objects.filter(category__iexact="politics")
    context = {'post': post}
    return render(request, 'news/category/politics.html', context)


def sports_page(request):
    post = Post.objects.filter(category__iexact="sports")
    context = {'post': post}
    return render(request, 'news/category/sports.html', context)


def tech_page(request):
    post = Post.objects.filter(category__iexact="tech")
    context = {'post': post}
    return render(request, 'news/category/tech.html', context)

def category_page(request):
    return render(request, 'news/category-page.html')


def weather_page(request):
    post = Post.objects.filter(category__iexact="weather")
    context = {'post': post}
    return render(request, 'news/category/weather.html', context)


