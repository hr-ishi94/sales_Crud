from django.db import models

class Sales(models.Model):
    product_ID = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=100)
    date=models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount=models.DecimalField(max_digits=4, decimal_places=2,default=0.00)
    units_sold=models.IntegerField()
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return str(self.product_ID)