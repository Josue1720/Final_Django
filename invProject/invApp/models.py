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