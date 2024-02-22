import os

def ad_image_upload_path(instance, filename):
    # instance - экземпляр модели AdImage
    # filename - оригинальное имя файла
    ad_base_model_id = instance.ad.id
    # Создайте путь к файлу в формате "media/ad_images/{ad_base_model_id}/{filename}"
    return os.path.join('ad_images', str(ad_base_model_id), filename)