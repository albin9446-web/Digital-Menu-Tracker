from django.contrib import admin
from .models import Category, MenuItem, Order


# 🔹 MenuItem Admin (clean view)
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available')
    list_filter = ('available',)


# 🔹 Order Admin (track orders easily)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'status')
    list_filter = ('status',)


# 🔹 Category (simple)
admin.site.register(Category)