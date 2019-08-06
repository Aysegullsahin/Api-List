from rest_framework import serializers

from .models import Category
from .models import Api

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'slug']

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = ('__all__')