from rest_framework import serializers

from Orders import models


class OrderSerializer(serializers.ModelSerializer):

    """def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(models.OrderModels, self).__init__(many=many, *args, **kwargs)"""

    class Meta:
        model = models.OrdersModel
        fields = ('user', 'product', 'quantity')
