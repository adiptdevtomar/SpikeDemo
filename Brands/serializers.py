from rest_framework import serializers
from Brands import models


class BrandSerializer(serializers.ModelSerializer):
    """Serializes Brand Data"""

    class Meta:
        model = models.BrandModel
        fields = ['name','description','brand_logo']
