from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm
)
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from PIL import Image


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


class UserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
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

    password = None

    class Meta:
        model = User
        fields = ['email', 'first_name','last_name', 'blood_group', 'gender', 'date_of_birth', 'phone_number', 'district', 'local_level']


class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""

    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Old Password',
            }
        ))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'New Password',
            }
        ))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'New Password',
            }
        ))


class PhotoForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ('display_photo', 'x', 'y', 'width', 'height', )

    def save(self):
        photo = super(PhotoForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(photo.file)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
        resized_image.save(photo.file.path)

        return photo