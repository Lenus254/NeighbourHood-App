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

    def test_delete_area(self):
        self.new_area.delete_hood()
        areas = Area.objects.all()
        self.assertTrue(len(areas-1) )

    # def test_update_bio(self):
    #     self.new_profile.save_profile()
    #     self.new_profile = Profile.objects.get(id=1)
    #     profile = self.new_profile
    #     profile.update_bio('updated user-bio')
    #     self.updated_profile = Profile.objects.get(id=1)
    #     self.assertEqual(self.updated_profile.bio,'updated user-bio')
