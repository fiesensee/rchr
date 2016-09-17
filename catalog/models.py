from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Article(models.Model):
    newspaper = models.ForeignKey('Newspaper')
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    text = models.TextField()
    timestamp = models.DateTimeField()
    source = models.CharField(max_length=100, default='NaN')
    judging = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Newspaper(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name