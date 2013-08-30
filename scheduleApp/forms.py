from django import forms
from django.forms import ModelForm
from scheduleApp.models import User, Course, Membership

class ShoppingForm(forms.Form):
	is_shopping = forms.BooleanField(required=False)

class ProfileForm(forms.Form):
	year_choices = (
		('Freshman', 	'Freshman'),
		('Sophomore', 'Sophomore'),
		('Junior', 		'Junior'),
		('Senior', 		'Senior'),
		('Graduate', 	'Graduate'),
	)
	year = forms.ChoiceField(year_choices)
