from rest_framework import serializers
from Products import models
from django.conf import settings


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProductModel
        fields = ['name','price','quantity','description','brand','image']

class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProductModel
        fields = ['id','name','price','image']

"""
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImageModel
        fields = ['image']"""
