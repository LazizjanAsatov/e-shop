from django.contrib import admin

# Register your models here.
from . models import *

class ImagesTublerinlineAdmin(admin.TabularInline):
    model = Images

class TagTublerinlineAdmin(admin.TabularInline):
    model = Tag

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesTublerinlineAdmin,TagTublerinlineAdmin]


admin.site.register(Images)
admin.site.register(Tag)
admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Filter_Price)
admin.site.register(Product,ProductAdmin)