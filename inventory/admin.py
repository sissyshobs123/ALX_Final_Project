from django.contrib import admin
from .models import Item, Category


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price", "date_added")
    search_fields = ("name", "category__name")
    list_display_links = ('name',) 
    list_filter = ("category",)
    ordering = ("price",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links =('name',)
    search_fields = ("name",)
