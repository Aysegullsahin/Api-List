from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import  SearchFilter, OrderingFilter
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.request import Request

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
        query = Api.objects.filter()
        if request.query_params.get('search') == '':
            api_name = request.query_params.get('api_name', None)
            description = request.query_params.get('description', None)
            if api_name:
                query = query.filter(api_name__icontains=api_name)
            if description:
                query = query.filter(description__icontains=description)
        serializer = ApiSerializer(query, many=True)
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
        if not api:
            return  Response(status=status.HTTP_404_NOT_FOUND)
        api.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, slug):
        api = Api.objects.filter(slug=slug).first()
        serializer = ApiSerializer(api, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
