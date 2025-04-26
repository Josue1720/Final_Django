from django.db import models

# Create your models here.
class Products(models.Model):
    product_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique = True) #Stock Keeping Unit
    price = models.FloatField(max_length = 100)
    quantity = models.IntegerField()
    supplier_name = models.CharField(max_length = 500)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Product"  # singular name in Admin
        verbose_name_plural = "Products" 
        
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=100, unique=True)
    password=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.username #para dae magdisplay username
    
    
    class Meta: #Purpose: para maayos yung pangalan na lumalabas sa Django Adm
        verbose_name = "User"  # singular name in Admin
        verbose_name_plural = "Users" 