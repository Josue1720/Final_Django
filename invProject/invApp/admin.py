from django.contrib import admin

# Register your models here.
from .models import Products #import Products model
from .models import Users
class ProductsAdmin(admin.ModelAdmin): #create a class for admin site
    list_display = ('name', 'price', 'quantity','supplier_name','sku',) #display these fields in admin site    
    search_fields = ('name',) #search by product name
    list_filter = ('price',) #filter by product price

admin.site.register(Products,ProductsAdmin)

class UsersAdmin(admin.ModelAdmin): #create a class for admin site
    search_fields=('username'),
    list_display =('user_id','username','password') #display these fields in admin site

admin.site.register(Users,UsersAdmin)
