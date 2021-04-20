from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from .utils import upload_image_path, compressImage


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError(_('Email is required.'))
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_active', True)
        kwargs.setdefault('is_superuser', True)
        if kwargs.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        return self.create_user(email, password, **kwargs)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    BLOOD_GROUPS = (
        ('A_P', 'A+'),
        ('A_N', 'A-'),
        ('B_P', 'B+'),
        ('B_N', 'B-'),
        ('AB_P', 'AB+'),
        ('AB_N', 'AB+'),
        ('O_P', 'O+'),
        ('O_N', 'O-'),
    )
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    email = models.EmailField(_('Email Address'), unique=True)
    first_name = models.CharField(_('First Name'), max_length=254)
    last_name = models.CharField(_('Last Name'), max_length=254)
    display_photo = models.ImageField(_('Display Photo'), upload_to=upload_image_path, default='default.png')
    date_of_birth = models.DateField(_('Date Of Birth'))
    gender = models.CharField(_('Gender'), max_length=1, choices=GENDERS)
    blood_group = models.CharField(max_length=4, choices=BLOOD_GROUPS)
    is_donor = models.BooleanField(_('Is Donor'), default=True)
    district = models.CharField(_('District'), max_length=254)
    local_level = models.CharField(_('Local Level'), max_length=254)
    phone_number = models.CharField(_('Phone Number'), max_length=10, unique=True)
    date_joined = models.DateTimeField(_('Date Joined'), default=timezone.now)
    is_active = models.BooleanField(_('Is Active'), default=True)
    is_staff = models.BooleanField(_('Is Staff'), default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth', 'gender', 'blood_group', 'phone_number', 'district', 'local_level']

    def __str__(self):
         return self.email
    
    def save(self, *args, **kwargs):
        self.display_photo = compressImage(self.display_photo)
        return super(CustomUser, self).save(*args, **kwargs)

    def age(self):
        import datetime
        return int((datetime.date.today() - self.date_of_birth).days / 365.25  )
    
    class Meta:
        verbose_name = 'User'