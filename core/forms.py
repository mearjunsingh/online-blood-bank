from django import forms
from django.db.models import fields
from . import models


class RequestForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""
    
    blood_group = forms.ChoiceField(label='Blood Group', widget=forms.Select(
        attrs={
            'class': 'form-control',
            'placeholder': 'Blood Group'
        }
    ))

    class Meta:
        model = models.Request
        fields = ['blood_group', 'for_date', 'district', 'local_level']
        widgets = {
            'for_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Local Level', 'type': 'date'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Local Level'}),
            'local_level': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Local Level'}),
        }