from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from area.models import Area

# Create your views here.
@login_required(login_url='login')
def index(request):
    neighbourhoods = Area.objects.all()
    ctx = {
        "hoods" : neighbourhoods
    }
    return render(request, 'index.html', ctx)
