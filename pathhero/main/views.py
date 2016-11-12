from django.shortcuts import render
from .forms import LocationInputForm
import json, os


# Create your views here.


def index(request):
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	MAPS_KEY = json.loads(open(BASE_DIR + '/config.json', 'rb').read())['MAPS_KEY']
	form = LocationInputForm()
	return render(request, 'main/index.html', {'MAPS_KEY': MAPS_KEY, 'form': form})
