import uuid

def user_profile_image_file(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return f'{instance.id}/{filename}'


def request_blood_image_file(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return f'{instance.requested_by.id}/requests/{filename}'