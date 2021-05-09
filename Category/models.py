from django.db import models
from django.utils.crypto import get_random_string


def get_image_filename(instance, filename):
    id = instance.id
    return "images/Categories/" + id + ".jpg"


class CategoryModel(models.Model):
    """Model for different product Categories"""
    id = models.CharField(primary_key=True, max_length=3)
    name = models.CharField(max_length = 80, blank = False)
    description = models.CharField(max_length = 500, blank = False)
    category_logo = models.ImageField(upload_to = get_image_filename,verbose_name="image")

    def save(self, *args, **kwargs):
        self.id = get_random_string(3)
        super(CategoryModel,self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}:{self.description}"
