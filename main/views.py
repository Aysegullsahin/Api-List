from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Api
from .serializers import CategorySerializer, ApiSerializer


class CategoryListAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CategoryDetail(APIView):
    def get(self, request, slug):
        category = Category.objects.filter(slug=slug).first()
        if not category:
            return Response({'detail': 'Error'}, status=404)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=200)

    def delete(self, request, slug):
        category = Category.objects.filter(slug=slug)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, slug):
        category = Category.objects.filter(slug=slug).first()
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApiListAPIView(APIView):
    def get(self, request):
        apis = Api.objects.all()
        serializer = ApiSerializer(apis, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiDetail(APIView):
    def get(self, request,slug):
        api = Api.objects.filter(slug=slug).first()
        serializer = ApiSerializer(api)
        return Response(serializer.data, status=200)

    def delete(self, request, slug):
        api = Api.objects.filter(slug=slug).first()
        api.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   
        
