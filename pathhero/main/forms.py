from __future__ import unicode_literals
from django import forms
from .models import Building


class LocationInputForm(forms.Form):
	start = forms.ModelChoiceField(queryset=Building.objects.order_by('name'), label='Start')
	mid = forms.ModelChoiceField(queryset=Building.objects.order_by('name'), label='Mid')
	end = forms.ModelChoiceField(queryset=Building.objects.order_by('name'), label='End')