from django.contrib import admin

from .models import Product,Category
class Productadmin(admin.ModelAdmin):
    list_display=('id','name','image','price','is_published','created_at')
    list_display_links = ('id','name')
    list_filter = ('price','created_at')
    list_editable = ('is_published',)
    search_fields = ('name','price')
    ordering=('price',)

admin.site.register(Product,Productadmin)
admin.site.register(Category)
