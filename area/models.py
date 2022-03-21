from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Area(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='admin')
    hoodimage = CloudinaryField()
    description = models.CharField(max_length=60)
    police_number = models.IntegerField(null=True, blank=True)
    emergency_no = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} hood'

    def create_hood(self):
        self.save()

    def update_hood(self):
      self.save()

    def delete_hood(self):
        self.delete()

    @classmethod
    def find_hood(cls, hood_id):
        return cls.objects.filter(id=hood_id)
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='profile')
    bio = models.CharField(blank=True, max_length=120)
    profile_pic = CloudinaryField(
        default="https://res.cloudinary.com/playboard/image/upload/v1626529829/vjytnast5wblft8xvy9p.jpg",
    )
    full_name = models.CharField(blank=True, max_length=120)
    profession = models.CharField(blank=True, max_length=120)
    email_address = models.EmailField(null=True, blank=True)
    # website_url= URLOrRelativeURLField(null=True,blank=True)
    # facebook =URLOrRelativeURLField(null=True,blank=True)
    # instagram = URLOrRelativeURLField(null=True,blank=True)
    # twitter = URLOrRelativeURLField(null=True,blank=True)
    mobile_number = models.IntegerField(null=True, blank=True)
    location = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)

    def __str__(self):
        return str(self.user)