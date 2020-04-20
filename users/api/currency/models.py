from django.db import models


class Currency(models.Model):
    currency_name=models.CharField(max_length=5)
    currency_value=models.DecimalField(max_digits=7, decimal_places=4)
    country=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


