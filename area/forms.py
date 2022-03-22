from django import forms
from django.contrib.auth.models import User
from .models import Profile, Posts, Business, Area


class EditProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ('user', 'location')
    
class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        exclude = ('admin',)

class BusinessForm(forms.ModelForm):
  class Meta:
    model = Business
    exclude = ('owner', 'hood', 'bs_logo')



class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ('user', 'hood')