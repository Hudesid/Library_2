from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'updated_at')
    list_filter = ('published_date', )
    search_fields = ('title', 'author')
