from django import forms
from django.db.models import fields
from . import models


class RequestForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""
    
    class Meta:
        model = models.Request
        fields = ['blood_group', 'for_date', 'district', 'local_level']
        widgets = {
            'blood_group': forms.Select(attrs={'class': 'form-control'}),
            'for_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'district': forms.Select(attrs={'class': 'form-control'}),
            'local_level': forms.Select(attrs={'class': 'form-control'}),
        }


class RequestUser(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RequestUser, self).__init__(*args, **kwargs)
        self.label_suffix = ""

    class Meta:
        model = models.Request
        fields = ['for_date', 'district', 'local_level']
        widgets = {
            'for_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'district': forms.Select(attrs={'class': 'form-control'}),
            'local_level': forms.Select(attrs={'class': 'form-control'}),
        }