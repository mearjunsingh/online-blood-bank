import uuid
import sys
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


def upload_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return f'{instance.id}/{filename}'


def compressImage(uploadedImage):
    imageTemproary = Image.open(uploadedImage)
    outputIoStream = BytesIO()
    imageTemproaryResized = imageTemproary.resize( (400, 300) ) 
    imageTemproaryResized.save(outputIoStream , format='JPEG', quality=40)
    outputIoStream.seek(0)
    uploadedImage = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % uploadedImage.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
    return uploadedImage