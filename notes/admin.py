from django.contrib import admin
from .models import Note

# Register your models here.


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "text",
        "created_at",
        "updated_at",
    )
