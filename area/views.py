from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

import area
from .forms import EditProfileForm, AreaForm, BusinessForm, PostForm
from area.models import Area, Profile, Posts, Business
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='login')
def index(request):
    neighbourhoods = Area.objects.all()
    ctx = {
        "hoods" : neighbourhoods
    }
    return render(request, 'index.html', ctx)

def new_area(request):
    if request.method == 'POST':
        form = AreaForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('index')
    else:
        form = AreaForm()
    return render(request, 'create_hood.html', {'form': form})

def join_area(request, id):
    try:
        area = Area.objects.get(id =id)
    except ObjectDoesNotExist:
        return Http404
    request.user.profile.location = area
    request.user.profile.save()
    return redirect('index')

def exit_area(request, id):
    try:
        area = Area.objects.get(id =id)
    except ObjectDoesNotExist:
        return Http404
    request.user.profile.location = None
    request.user.profile.save()
    return redirect('index')

def profile(request , username):
    user = User.objects.get(username=username)
    try:
        profile = Profile.objects.get(user=user.id)
        
    except ObjectDoesNotExist:
        raise Http404()
    businesses = Business.objects.filter(owner = profile)
    posts = Posts.objects.filter(user = profile)
    ctx = {
        "user": user,
        "profile" : profile,
        "businesses": businesses,
        "posts":posts
    }
    return render(request, 'profile.html', ctx)

def edit_profile(request, username):
    user = User.objects.get(username = username)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance = request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)

    else: 
        form = EditProfileForm(instance = request.user.profile)
    return render(request, 'edit_profile.html', {'form': form})

def view_area(request, hood_id):
    area= Area.objects.get(id =hood_id)
    business = Business.objects.filter(hood = area)
    posts = Posts.objects.filter(hood = area)
    posts = posts[::-1]
    ctx = {
        'hood': area,
        'business': business,
        'news': posts
    }
    return render(request, 'view_hood.html', ctx)

def add_business(request, hood_id):
    if request.method == 'POST':
        area = Area.objects.get(id =hood_id)
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            bs_form = form.save(commit=False)
            bs_form.hood = area
            bs_form.owner = request.user.profile
            bs_form.create_business()
            return redirect('view-hood', area.id)
    else:
        form = BusinessForm()

    return render(request, 'new_business.html', {"form" : form})

def new_post(request, hood_id):
    hood = Area.objects.get(id =hood_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.hood = hood
            news.user = request.user.profile
            news.save()
            return redirect('view-hood', hood.id)
    else:
        form = PostForm()
    return render(request, 'news.html', {'form': form})

def hood_members(request, hood_id):
    hood = Area.objects.get(id =hood_id)
    residents = Profile.objects.filter(location = hood)
    ctx ={
        'residents':residents
    }
    return render(request, 'hood_residents.html', ctx)

def search_business(request):
    if request.method == 'GET':
        name = request.GET.get("title")

        results = Business.objects.filter(bs_name__icontains=name).all()
        print(results)
        message = f'name'
        ctx = {
            'results': results,
            'message': message
        }
        return render(request, 'results.html', ctx)
    else:
        message = "You haven't searched for any image category"
    return render(request, "results.html")