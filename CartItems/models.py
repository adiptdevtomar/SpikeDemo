from django.db import models
from Cart.models import CartModel
from Products.models import ProductModel


class CartItemsModel(models.Model):
    """Model for Cart Items"""

    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank = False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['cart', 'product'], name='cartItem_key')
        ]

    def __str__(self):
        return f"{self.product_id}"
