from django.db import models


class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField ()
    product_category = models.CharField(max_length=40)
    product_image = models.ImageField(upload_to ='static/upload/')
    cut_price= models.IntegerField(null=True)
    product_price= models.IntegerField(default=0)
    product_ammount = models.CharField(max_length=30)


class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=500)
    mobile=models.IntegerField(range(11, 14))
    email=models.CharField(max_length=100)