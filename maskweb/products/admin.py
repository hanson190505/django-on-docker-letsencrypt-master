from django.contrib import admin
from products.models import Products, Suppliers, ProductDetail, Category


@admin.register(Suppliers)
class SuppliersAdmin(admin.ModelAdmin):
    list_display = ('s_name', 's_addr', 's_manager', 's_contact', 's_email', 's_mobile')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('item', 'item_child', 'pub_date')


class ProductDetailAdmin(admin.TabularInline):
    model = ProductDetail


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('category', 'pro_name', 'pro_desc', 'pro_keywords', 'pro_type', 'pro_supplier', 'pro_price')
    inlines = [ProductDetailAdmin, ]
