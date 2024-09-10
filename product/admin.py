from django.contrib import admin

from .models import Category,Customer,Payment,Product,Order

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Payment)
admin.site.register(Product)
admin.site.register(Order)

