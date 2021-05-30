from django.db import models
from django.db.models.deletion import RESTRICT
from django.conf import settings
User = settings.AUTH_USER_MODEL
from django.utils.text import slugify


class Request(models.Model):

    STATUS = (
        ('pending', 'Pending'),
        ('verified', 'Verified'),
        ('completed', 'Completed'),
    )
    
    requested_by = models.ForeignKey(User, on_delete = models.RESTRICT, related_name='requested_by')
    requested_date = models.DateField(auto_now_add=True)
    for_date = models.DateField()
    blood_group = models.ForeignKey('Blood', on_delete=RESTRICT)
    district = models.CharField(max_length=254)
    local_level = models.CharField(max_length=254)
    donated_by = models.ForeignKey(User, on_delete=RESTRICT, null=True, blank=True, related_name='donated_by')
    status = models.CharField(max_length=10, default='pending', choices=STATUS)

    def __str__(self):
        return f'{self.blood_group} by {self.requested_by}'


class Blood(models.Model):
    group = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.group)
        super().save(self, *args, **kwargs)

    def __str__(self):
        return self.group