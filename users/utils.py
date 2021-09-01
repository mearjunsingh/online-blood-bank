import uuid
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def user_profile_image_file(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return f'{instance.id}/{filename}'


def request_blood_image_file(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return f'{instance.requested_by.id}/requests/{filename}'


def email_donor(request):
    subject = 'Blood Donation: You have new request'
    html_message = render_to_string('mails/donor_mail_template.html', {'context' : request})
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER
    to = request.donated_by.email
    send_mail(subject, plain_message, from_email, [to], html_message=html_message)


def email_reciever(request):
    subject = 'Blood Donation: Found new donor'
    html_message = render_to_string('mails/reciever_mail_template.html', {'context' : request})
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER
    to = request.requested_by.email
    send_mail(subject, plain_message, from_email, [to], html_message=html_message)