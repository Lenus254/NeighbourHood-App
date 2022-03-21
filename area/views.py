from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm, AreaForm, BusinessForm, PostForm
from area.models import Area, Profile, Posts, Business

# Create your views here.
@login_required(login_url='login')
def index(request):
    neighbourhoods = Area.objects.all()
    ctx = {
        "hoods" : neighbourhoods
    }
    return render(request, 'index.html', ctx)

def new_hood(request):
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
