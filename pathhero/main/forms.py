from __future__ import unicode_literals
from django import forms


class LocationInputForm(forms.Form):
	origin = forms.CharField(label='From')
	destination = forms.CharField(label='To')


