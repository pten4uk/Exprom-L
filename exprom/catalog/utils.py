import os


def photo_directory_path(instance, filename):
    path = f'media/photos/{instance.product.category.name} {instance.product.number}/{filename}'
    if os.path.exists(path):
        os.remove(path)
    return path
