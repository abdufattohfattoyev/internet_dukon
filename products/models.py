from django.db import models

from users.models import User
from utility.models import BaseModel


class Category(BaseModel):
    title=models.CharField(max_length=100,null=False,blank=False,unique=True)
    description=models.TextField(null=True,blank=True)
    image=models.ImageField(upload_to="category/",null=True,blank=True)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Product(BaseModel):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=255,null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=True,blank=True)
    cover_pic=models.ImageField(upload_to="products/",null=False,blank=False)
    small_description=models.CharField(max_length=300)
    description=models.TextField(null=True,blank=True)
    tags=models.CharField(max_length=100,null=True,blank=True)
    quantity=models.IntegerField(default=0)


    def __str__(self):
        return self.title


class ProductImage(BaseModel):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="product/",null=False,blank=False)

    def __str__(self):
        return f"{self.product.title} rasmi"


class Cart(BaseModel):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    total_price=models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.product.name
