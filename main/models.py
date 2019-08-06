from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django import forms
from django.db.models import BooleanField


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    
    def __str__(self):
        return self.title
        
    def save(self, *arg, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*arg, **kwargs)


class Api(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    api_name = models.CharField(max_length=200)
    url = models.URLField(max_length=250)
    logo = models.ImageField(upload_to='api-logos/')
    description = models.TextField()
    officialapi = models.BooleanField(default=True)
    github = models.URLField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.api_name
    
    def save(self, *arg, **kwargs):
        self.slug = slugify(self.api_name)
        super(Api, self).save(*arg, **kwargs)    
