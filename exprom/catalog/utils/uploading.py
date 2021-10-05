import os


def upload_function(instance, filename):
    if hasattr(instance, 'content_object'):
        instance = instance.content_object

    path = f'media/products/{instance}/{filename}'

    if not os.path.exists(path):
        return path
    else:
        os.remove(path)
        return path
