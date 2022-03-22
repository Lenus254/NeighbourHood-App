from django.test import TestCase
from django.contrib.auth.models import User
from .models import Area, Posts, Profile, Business

# Create your tests here.
class AreaTestClass(TestCase):
    def setUp(self):
        self.new_area = Area(name="sach4",location="uthiru",description="peacefull area",police_number=9998999,emergency_no=89889)
      

    def test_instance(self):
        self.assertTrue(isinstance(self.new_area,Area))

    def test_save_area(self):
        self.new_area.create_hood()
        areas = Area.objects.all()
        self.assertTrue(len(areas) > 0)

class ProfilesTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='password')
        self.new_profile = Profile(bio="fighter",full_name="len",profession="dct",email_address="a@ymail.com",mobile_number=9878)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
        

class PostTestClass(TestCase):
    def setUp(self):
        self.new_post = Posts(title="wedding", details="my wedding")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Posts))

    def test_save_post(self):
        self.new_post.new_post()
        posts = Posts.objects.all()
        self.assertTrue(len(posts) > 0)


   

   