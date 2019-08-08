from django.db import models
from django.template.defaultfilters import slugify

class SingUP(models.Model):
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)


    def __str__(self):
        return self.username
    
    def save(self, *arg, **kwargs):
        self.slug = slugify(self.username)
        super(SingUP, self).save(*arg, **kwargs)    
