from django.contrib.auth.models import User
from rest_framework import serializers


# {
#     'username': 
#     'password1':
#     'password2':
#     'email':..
# }
# class RegisterSerializer(serializers.serializers):
#     username = serializers.CharField()
#     password1 = serializers.IntegerField()
#     password2 = serializers.IntegerField()
#     email = serializers.CharField()

#     def validate(self, data):
#         if data.get('password1') != password2:
#             return.. .
#         import ipdb; ipdb.set_trace()
