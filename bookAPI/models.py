from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=80)
    description = models.CharField(max_length=1000)
    isbn = models.CharField(max_length=13, help_text='Please supply a 13 digit-long ISBN.')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField(default=0)
    published_date = models.DateField()
    genre = models.CharField(max_length=50)