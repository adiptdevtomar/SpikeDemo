from django.db import models
from Category.models import CategoryModel
from django.utils.crypto import get_random_string


def get_image_filename(instance, filename):
    id = instance.id
    name = instance.name
    return "images/product_images/"+id+"/display_Image.jpg"


class ProductModel(models.Model):
    """Model for all products"""
    id = models.CharField(primary_key = True, max_length = 8)
    name = models.CharField(max_length = 80, blank = False)
    price = models.DecimalField(blank = False, decimal_places = 2, max_digits = 80)
    quantity = models.IntegerField(blank = False)
    description = models.CharField(max_length = 500, blank = False)
    category = models.ForeignKey(CategoryModel, to_field="id", on_delete=models.CASCADE)
    image = models.ImageField(upload_to = get_image_filename,verbose_name="image")
    #category

    def save(self, *args, **kwargs):
        self.id = get_random_string(8)
        super(ProductModel,self).save(*args, **kwargs)

    def saveUpdate(self, *args, **kwargs):
        super(ProductModel,self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}:{self.price}"


"""
class ImageModel(models.Model):
    Model for product images
    image = models.ImageField(upload_to = get_image_filename,verbose_name="image")
    details = models.ForeignKey(ProductModel,on_delete = models.CASCADE, related_name="product_images")"""
