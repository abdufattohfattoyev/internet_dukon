from django.contrib import admin
from .models import Cart,Category,Product,ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","title","status"]
    list_filter = ("title","status")
    search_fields = ("title",)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["id","user","product","quantity"]
    list_filter = ("product","user")
    search_fields = ("user","product")


class ProductImageAdmin(admin.TabularInline):
    extra = 1
    model = ProductImage
    fields = ["image"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id","title","original_price","selling_price","quantity"]
    list_filter = ["category","original_price"]
    search_fields = ["category","title","description"]
    inlines = [ProductImageAdmin]