from django.db import models
from django.conf import settings

from Products.models import ProductModel


class OrdersModel(models.Model):
    """Model for Orders"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete = models.CASCADE)
    quantity = models.IntegerField(blank = False)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'product'], name='orderItem_Key')
        ]

    def __str__(self):
        return f"{self.user}:{self.product}"
