from django.shortcuts import render
from .forms import LocationForm, MidpointForm
from django.forms.formsets import formset_factory

import json
import os

# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAPS_KEY = json.loads(open(BASE_DIR + '/config.json', 'rb').read())['MAPS_KEY']


def index(request):
	MidpointFormSet = formset_factory(MidpointForm, max_num=10, extra=1)
	if request.method == 'POST':
		form = LocationForm(request.POST)
		mids = MidpointFormSet(request.POST)
		if form.is_valid() and mids.is_valid():
			origin = form.cleaned_data['start']
			destination = form.cleaned_data['end']
			payload = {
				'MAPS_KEY': MAPS_KEY,
				'origin': origin,
				'midpoints': [(i['mid'].name, i['mid'].lat, i['mid'].lng) for i in mids.cleaned_data],
				'destination': destination
			}
			return render(request, 'main/directions.html', payload)
	else:
		form = LocationForm()
		MidpointFormSet = formset_factory(MidpointForm, max_num=10, extra=1)

	return render(request, 'main/index.html', {'MAPS_KEY': MAPS_KEY, 'mid_formset': MidpointFormSet, 'form': form})

