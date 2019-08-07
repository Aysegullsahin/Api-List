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
        # exclude = ['id']
        fields = ('__all__')
    
    def update(self, instance, validated_data):
        instance.category = validated_data.get('category', instance.category)
        instance.api_name = validated_data.get('api_name', instance.api_name)
        instance.url = validated_data.get('url', instance.url)
        instance.description = validated_data.get('description', instance.description)
        instance.officialapi = validated_data.get('officialapi', instance.officialapi)
        instance.github = validated_data.get('github', instance.github)
        instance.email = validated_data.get('email', instance.email)
        instance.twitter = validated_data.get('twitter', instance.twitter)
        instance.created_date = validated_data.get('created_date', instance.created_date)
        instance.save()
        return instance