import datetime
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from . import utils
from core.models import Blood


class CustomUserManager(BaseUserManager):
    """Custom user manager"""

    def create_user(self, email, password, **kwargs):
        """Create a new user profile"""
        if not email:
            raise ValueError(_('User must have an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self, email, password, **kwargs):
        """Create a new superuser profile"""
        user = self.create_user(email, password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    email = models.EmailField(_('Email Address'), unique=True)
    first_name = models.CharField(_('First Name'), max_length=254)
    last_name = models.CharField(_('Last Name'), max_length=254)
    display_photo = models.ImageField(_('Display Photo'), upload_to=utils.user_profile_image_file, default='default.png')
    date_of_birth = models.DateField(_('Date Of Birth'))
    gender = models.CharField(_('Gender'), max_length=1, choices=GENDERS)
    blood_group = models.ForeignKey(Blood, on_delete=models.RESTRICT)
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

    @property
    def age(self):
        return int((datetime.date.today() - self.date_of_birth).days / 365.25)
    
    def save(self, *args, **kwargs):
        if not self.id:
            new_image = utils.compress_image_on_upload(self.display_photo)
            self.display_photo = new_image
        super().save(*args, **kwargs)
    
    def __str__(self):
         return self.email
    
    class Meta:
        verbose_name = _('User')