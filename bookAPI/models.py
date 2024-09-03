import os

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from coreApp.services.rabbitmq import AmqpMessage, FastPublisher

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=80)
    description = models.CharField(null=True, blank=True, max_length=1000)
    isbn = models.CharField(max_length=13, help_text='Please supply a 13 digit-long ISBN.')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField(default=0)
    published_date = models.DateField()
    genre = models.CharField(max_length=50)

    def __str__(self):
        return "{}, Author: {}, ISBN: {}".format(self.title, self.author, self.isbn)
    
    using = 'books'

publisher = FastPublisher(name=os.getenv('BOOKS_EXCHANGE'))

# Signals go here.
@receiver(post_save, sender=Book)
def new_book_created(sender, instance, created, **kwargs):
    if created:
        print(f"New book added: {instance.title} by {instance.author}")

        from .serializers import BookSerializer
        serializer = BookSerializer(instance)

        publisher.publish(message=AmqpMessage(
            routing_key=os.getenv('BOOKS_CREATED_ROUTING_KEY'),
            body=serializer.data
        ))