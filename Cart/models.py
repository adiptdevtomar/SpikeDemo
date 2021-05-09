from django.db import models
from django.conf import settings
from django.utils.crypto import get_random_string


class CartModel(models.Model):
    """Model for Cart"""

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    cart_id = models.CharField(primary_key = True, max_length = 8)
    tax_percentage = models.DecimalField(max_digits=10, decimal_places=5, default=0.085)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default = 0.00)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2, default = 0.00)
    total = models.DecimalField(max_digits=12, decimal_places=2, default = 0.00)

    def save(self, *args, **kwargs):
        self.cart_id = get_random_string(8)
        super(CartModel,self).save(*args, **kwargs)

    def saveUpdate(self, *args, **kwargs):
        super(CartModel,self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.cart_id}:{self.total}"
