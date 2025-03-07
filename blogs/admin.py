from django.contrib import admin
from .models import Blog

# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "blog_contents",
        "user",
        "created_at",
        "updated_at",
    )
