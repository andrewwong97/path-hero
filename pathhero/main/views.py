from django.shortcuts import render
from .forms import LocationInputForm
import json
import os

# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAPS_KEY = json.loads(open(BASE_DIR + '/config.json', 'rb').read())['MAPS_KEY']


def index(request):
	if request.method == 'POST':
		form = LocationInputForm(request.POST)
		if form.is_valid():
			origin = form.cleaned_data['start']
			destination = form.cleaned_data['end']
			print origin, destination
			payload = {
				'MAPS_KEY': MAPS_KEY,
				'form': form,
				'origin': origin,
				'destination': destination
			}
			return render(request, 'main/directions.html', payload)
	else:
		form = LocationInputForm()

	return render(request, 'main/index.html', {'MAPS_KEY': MAPS_KEY, 'form': form})

