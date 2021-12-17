from django.contrib import admin

# Register your models here.
from daomi.comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name']