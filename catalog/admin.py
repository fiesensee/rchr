from django.contrib import admin

# Register your models here.

from .models import Article, Newspaper

admin.site.register(Article)
admin.site.register(Newspaper)