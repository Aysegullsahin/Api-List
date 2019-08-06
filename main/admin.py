from django.contrib import admin

from .models import Api
from .models import Category

admin.site.register(Api)
admin.site.register(Category)