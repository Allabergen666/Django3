from django.contrib import admin

from django.utils.safestring import mark_safe
from .models import Product , Category, Comment
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=['category', 'name_product', 'price', 'description', 'get_image']
    list_filter=['category']
    search_fields=['category', 'name_product', 'price']
    list_editable=['price', 'description']

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f"<img src={obj.image.url} width='100px'>")
        else:
            return "Not image"


class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']
    search_fields=['name']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['username', 'comment', 'product']
    list_filter = ['product']
    search_fields = ['username', 'product']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)