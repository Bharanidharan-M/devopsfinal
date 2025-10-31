from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'published_date')
    list_display_links = ('id', 'title')
    list_editable = ('author', 'published_date')
    search_fields = ('title', 'author')
    list_filter = ('author', 'published_date')
    date_hierarchy = 'published_date'
    ordering = ('-id',)
    list_per_page = 25

    # Show save buttons on top and bottom of the change form
    save_on_top = True
    actions = ['delete_selected']
    actions_on_top = True
    actions_on_bottom = True

    # Field layout in the change form
    fields = (
        'title',
        'author',
        'published_date',
    )
