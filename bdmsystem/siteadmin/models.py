from django.db import models

# Create your models here.
class Stock(models.Model):
    bloodgroup = models.CharField(max_length=10)
    unit = models.PositiveIntegerField(default=0)


    class Meta:
        db_table ='stock'
