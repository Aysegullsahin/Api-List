from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response    
from rest_framework.views import APIView


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username and password:
            user = User.objects.filter(username=username).first()          
            if user and authenticate(username=username, password=password):
                login(request, user)
        return Response(status=200)
    
class LogoutView(APIView): 
    def get(self,request):            
        logout(request)
        return Response(status=200)
     