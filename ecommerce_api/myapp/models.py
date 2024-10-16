from django.db import models
from base.models import BaseModel

# Create your models here.

class Customer(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    contact_number = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Product(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
class Order(BaseModel):
    order_number = models.CharField(max_length=20, unique=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    address = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.order_number:
            last_order = Order.objects.order_by('order_number').last()
            if last_order:
                order_num = int(last_order.order_number[3:]) + 1
            else:
                order_num = 1
            self.order_number = f'ORD{order_num:05}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
