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

    # def test_delete_area(self):
    #     self.new_area.delete_hood()
    #     areas = Area.objects.all()
    #     self.assertTrue(len(areas-1) )

    def test_update_area(self):
        self.new_area.create_hood()
        self.new_area = Area.objects.get(id=1)
        areas = self.new_area
        areas.update_hood('updated new_area')
        self.updated_area = Area.objects.get(id=1)
        self.assertEqual(self.updated_area.hood,'updated new_area')
