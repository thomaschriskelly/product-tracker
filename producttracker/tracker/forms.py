from django import forms

class ProductForm(forms.Form):
    description = forms.CharField(label='', max_length=32)
