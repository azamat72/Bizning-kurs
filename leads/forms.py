from django import forms
from django.forms.widgets import Input, Textarea
from .models import Lead
from django.forms import ModelForm, TextInput



class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['familiyasi', 'ismi', 'yoshi', 'full', 'agent']

        widgets = {
            "familiyasi": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Familiyasi'
            }),
            "ismi": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ismi'
            }),
            "yoshi": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Yoshi'
            }),
            "full": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tarjimai hol'
            }),
        }  
            

class LeadForm(forms.Form):
    familiyasi = forms.CharField()
    ismi = forms.CharField()
    yoshi = forms.IntegerField(min_value=0)
    full = forms.Textarea()
    