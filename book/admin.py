from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'author',
                    'journal',
                    'published_date',
                    'publisher')
    
    search_fields = ('name',
                     'author',
                     'journal',
                     'publisher')
    
    list_filter = ('published_date',
                   'publisher')
