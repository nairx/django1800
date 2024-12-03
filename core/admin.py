from django.contrib import admin
from core.models import todo,product

class todoadmin(admin.ModelAdmin):
    list_display=("task",)
admin.site.register(todo,todoadmin)

class productadmin(admin.ModelAdmin):
    list_display=['id','name','price','desc','url']
    
admin.site.register(product,productadmin)
