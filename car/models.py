from django.db import models

# No "from .models import Car" here!

class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # ... your other fields ...

    def __str__(self):
        return self.name