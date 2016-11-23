from django.test import TestCase
from .models import Building


class BuildingsTest(TestCase):

	def setUp(self):
		Building.objects.create(name='AMR 1', lat=1.0, lng=1.0)
		self.b = Building.objects.get(name='AMR 1')

	def test_building_name(self):
		self.assertTrue(isinstance(self.b, Building))
		self.assertEqual(self.b.__unicode__(), self.b.name)

	def test_building_lat(self):
		self.assertEqual(self.b.lat, 1.0)

	def test_building_lng(self):
		self.assertEqual(self.b.lng, 1.0)

