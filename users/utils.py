import uuid
from io import BytesIO
from PIL import Image
from django.core.files import File


def user_profile_image_file(instance, filename):
    """Generate file path for new recipe image"""
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return f'{instance.id}/{filename}'

def compress_image_on_upload(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=70)
    new_image = File(im_io, name=image.name)
    return new_image