from django import forms
from django.db.models import fields
from . import models


class RequestForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""

    image = forms.ImageField(label='Image (Optional)', required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = models.Request
        fields = ['blood_group', 'for_date', 'district', 'local_level', 'image']
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
    
    image = forms.ImageField(label='Image (Optional)', required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = models.Request
        fields = ['for_date', 'district', 'local_level', 'image']
        widgets = {
            'for_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'district': forms.Select(attrs={'class': 'form-control'}),
            'local_level': forms.Select(attrs={'class': 'form-control'}),
        }