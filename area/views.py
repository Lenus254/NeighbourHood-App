from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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