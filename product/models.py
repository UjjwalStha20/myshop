from django.db import models

from django.db import models
from django.utils.html import mark_safe



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    storage =models.CharField(max_length=12)
    description = models.TextField(null= True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='uploads/',blank=True, null= True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)

    class Meta:
        ordering = ('-order_date',)

    def __str__(self):
        return f"Order {self.id} by {self.customer}"


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    totalbill = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-payment_date',)


    def __str__(self):
        return f"Payment {self.id} for Order {self.order.id}"


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100 )
    email = models.EmailField(max_length=255, unique=True )
    phone = models.CharField(max_length=15 ,  null= True , blank= True)
    address = models.TextField(max_length=100)
    password = models.CharField(max_length=20, null= True , blank= True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

