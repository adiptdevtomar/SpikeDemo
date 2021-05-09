from rest_framework import serializers

from CartItems.models import CartItemsModel


class CartItemSerializer(serializers.ModelSerializer):
    """Serializer for Cart Item"""

    class Meta:
        model = CartItemsModel
        fields = ['cart', 'product', 'quantity']

class RemoveCartItemSerializer(serializers.ModelSerializer):
    """Serializer for removing item from Cart"""

    class Meta:
        model = CartItemsModel
        fields = ['cart', 'product']
