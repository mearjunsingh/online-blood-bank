import uuid

def user_profile_image_file(instance, filename):
    """Generate file path for new recipe image"""
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return f'{instance.id}/{filename}'