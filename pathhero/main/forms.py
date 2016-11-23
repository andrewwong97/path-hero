from __future__ import unicode_literals
from django import forms
from .models import Building


class LocationForm(forms.Form):
	start = forms.ModelChoiceField(queryset=Building.objects.order_by('name'), label='Start')
	end = forms.ModelChoiceField(queryset=Building.objects.order_by('name'), label='End')


class MidpointForm(forms.Form):
	mid = forms.ModelChoiceField(queryset=Building.objects.order_by('name'), label='Mid', required=False)
