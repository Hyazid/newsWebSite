from django.contrib import admin
from .models import Article
# Register your models here.
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'author']
admin.site.register(Article, ArticlesAdmin)
