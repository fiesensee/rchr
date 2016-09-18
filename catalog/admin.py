from django.contrib import admin

# Register your models here.

from .models import Article, Newspaper, Catalog

admin.site.register(Article)
admin.site.register(Newspaper)
admin.site.register(Catalog)