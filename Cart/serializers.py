from rest_framework import serializers

from Cart import models


class CartSerializer(serializers.ModelSerializer):
    """Serializer for Cart"""

    class Meta:
        model = models.CartModel
        fields = ['user', 'cart_id', 'tax_amount','subtotal','total', 'tax_percentage']
