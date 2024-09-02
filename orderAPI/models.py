from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length = 254)

    def __str__(self):
        return self.email
    
    using = 'orders'

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    order_date = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (("P","Pending"), ("S", "Shipped"), ("D", "Delivered"), ("C", "Cancelled"))
    status = models.CharField(choices = STATUS_CHOICES, max_length=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    made_by_user = models.ForeignKey(User, on_delete=models.CASCADE)

    using = 'orders'

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=13, help_text='Please supply a 13 digit-long ISBN.')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField(default=0)
    orders = models.ManyToManyField(Order, through="BookLine")

    def __str__(self):
        return self.isbn
    
    using = 'orders'

class BookLine(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    related_to_book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    placed_in_order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)

    using = 'orders'