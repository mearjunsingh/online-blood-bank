from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""

    username = forms.EmailField(label='Email Address', widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email Address',
            'id' : 'id_email',
            'autofocus' : 'true'
            }
        ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            }
        ))


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""

    GENDERS = (
        ('', 'Choose One'),
        ('M', 'Male'),
        ('F', 'Female'),
    )

    BLOOD_GROUPS = (
        ('', 'Choose One'),
        ('A_P', 'A+'),
        ('A_N', 'A-'),
        ('B_P', 'B+'),
        ('B_N', 'B-'),
        ('AB_P', 'AB+'),
        ('AB_N', 'AB+'),
        ('O_P', 'O+'),
        ('O_N', 'O-'),
    )

    email = forms.EmailField(label='Email Address', widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email Address',
            }
        ))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'First Name',
            }
        ))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Last Name',
            }
        ))
    date_of_birth = forms.DateField(label='Date Of Birth', widget=forms.DateInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Date Of Birth',
            'type': 'date'
        }
    ))
    phone_number = forms.IntegerField(label='Phone Number', widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Phone Number'
        }
    ))
    gender = forms.ChoiceField(label='Gender', widget=forms.Select(
        attrs={
            'class': 'form-control',
            'placeholder': 'Gender'
        }
    ), choices=GENDERS)
    blood_group = forms.ChoiceField(label='Blood Group', widget=forms.Select(
        attrs={
            'class': 'form-control',
            'placeholder': 'Blood Group'
        }
    ), choices=BLOOD_GROUPS)
    district = forms.CharField(label='District', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'District',
            }
        ))
    local_level = forms.CharField(label='Local Level', widget=forms.TextInput(
    attrs={
        'class': 'form-control',
        'placeholder': 'Local Level',
        }
    ))
    password1 = forms.CharField(label='Choose Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Choose Password',
            }
        ))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password',
            }
        ))

    class Meta:
        model = User
        fields = ['email', 'first_name','last_name', 'blood_group', 'gender', 'date_of_birth', 'phone_number', 'district', 'local_level', 'password1', 'password2']
