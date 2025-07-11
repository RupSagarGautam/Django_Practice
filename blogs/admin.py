from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('title', 'author', 'created_at', 'updated_at', 'image')
=======
    list_display = ('title', 'author', 'created_at', 'updated_at')
>>>>>>> 9b1649bc10d0b866b398f2d320712c705551a5ac

admin.site.register(Blog, BlogAdmin)
