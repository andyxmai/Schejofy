from django import forms

class ShoppingForm(forms.Form):
    is_shopping = forms.BooleanField(required=False)