from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=True)


class Post(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=250, null=False, blank=True)
    content = models.TextField(null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.PROTECT)


 