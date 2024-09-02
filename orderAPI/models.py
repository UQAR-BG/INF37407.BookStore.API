from django.db import models

# Create your models here.
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    order_date = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (("P","Pending"), ("S", "Shipped"), ("D", "Delivered"), ("C", "Cancelled"))
    status = models.CharField(choices = STATUS_CHOICES, max_length=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    made_by_user = models.ForeignKey("User", on_delete=models.CASCADE)
    books = models.ManyToManyField("Book")