from django.contrib import admin
from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'language', 'release_date', 'file_type')
    list_filter = ('genre', 'language', 'file_type', 'release_date')
    search_fields = ('title', 'author__name', 'summary')
    date_hierarchy = 'release_date'

    fieldsets = (
        ('Book Information', {
            'fields': ('title', 'author', 'genre', 'language', 'release_date', 'summary')
        }),
        ('File Details', {
            'fields': ('file', 'file_type')
        }),
    )