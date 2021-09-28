
def photo_directory_path(instance, filename):
    return f'media/photos/{instance.product.number}/{filename}'
