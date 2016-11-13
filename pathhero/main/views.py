from django.shortcuts import render
from .forms import LocationInputForm
import json, os


# Create your views here.


def index(request):
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	MAPS_KEY = json.loads(open(BASE_DIR + '/config.json', 'rb').read())['MAPS_KEY']

	origin = ""
	dest = ""
	if request.method == 'POST':
		form = LocationInputForm(request.POST)
		if form.is_valid():
			origin = form.cleaned_data['origin']
			dest = form.cleaned_data['destination']
	else:
		form = LocationInputForm()

	load = {
		'MAPS_KEY': MAPS_KEY,
		'form': form,
		'origin': origin,
		'destination': dest
	}
	return render(request, 'main/index.html', load)
