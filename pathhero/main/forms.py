from __future__ import unicode_literals
from django import forms
from .models import Building


class LocationInputForm(forms.Form):
	start = forms.ModelChoiceField(queryset=Building.objects.all(), label='Start')
	mid = forms.ModelChoiceField(queryset=Building.objects.all(), label='Midpoint')
	end = forms.ModelChoiceField(queryset=Building.objects.all(), label='End')