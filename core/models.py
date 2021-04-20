from django.db import models
from django.db.models.deletion import RESTRICT
from django.contrib.auth import get_user_model
User = get_user_model()


class Request(models.Model):
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
    STATUS = (
        ('pending', 'Pending'),
        ('verified', 'Verified'),
        ('completed', 'Completed'),
    )
    requested_by = models.ForeignKey(User, on_delete = models.RESTRICT, related_name='requested_by')
    requested_date = models.DateField()
    for_date = models.DateField()
    blood_group = models.CharField(max_length=4, choices=BLOOD_GROUPS)
    district = models.CharField(max_length=254)
    local_level = models.CharField(max_length=254)
    donated_by = models.ForeignKey(User, on_delete=RESTRICT, null=True, blank=True ,related_name='donated_by')
    status = models.CharField(max_length=10, choices=STATUS)

    def __str__(self):
        return f'{self.blood_group} by {self.requested_by}'