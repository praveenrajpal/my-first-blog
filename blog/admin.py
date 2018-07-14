from django.contrib import admin

from .models import Post, Movies

# Register your models here.

admin.site.register(Post)
admin.site.register(Movies)