from rest_framework import serializers
from Category import models


class CategorySerializer(serializers.ModelSerializer):
    """Serializes Category Data"""

    class Meta:
        model = models.CategoryModel
        fields = ['id', 'name','description','category_logo']
