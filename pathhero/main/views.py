from django.shortcuts import render
from .forms import LocationForm, MidpointForm
from django.forms.formsets import formset_factory
from django.views import View

import json
import os

# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAPS_KEY = json.loads(open(BASE_DIR + '/config.json', 'rb').read())['MAPS_KEY']

class IndexView(View):
	form_class = LocationForm
	MidpointFormSet = formset_factory(MidpointForm, max_num=10)

	def get(self, request):
		form = self.form_class()
		context = {
			'MAPS_KEY': MAPS_KEY,
			'mid_formset': self.MidpointFormSet,
			'form': form
		}
		return render(request, 'main/index.html', context)

	def post(self, request):
		form = self.form_class(request.POST)
		mids = self.MidpointFormSet(request.POST)
		context = {}
		if form.is_valid() and mids.is_valid():
			origin = form.cleaned_data['start']
			destination = form.cleaned_data['end']
			context = {
				'MAPS_KEY': MAPS_KEY,
				'origin': origin,
				'midpoints': [(i['mid'].name, i['mid'].lat, i['mid'].lng) for i in mids.cleaned_data if i],
				'destination': destination
			}
		return render(request, 'main/directions.html', context)