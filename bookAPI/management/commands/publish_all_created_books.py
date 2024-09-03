import os

from django.core.management.base import BaseCommand

from bookAPI.models import Book, BookSerializer
from coreApp.services.rabbitmq import AmqpMessage, FanoutPublisher

class Command(BaseCommand):
    help = "Publishes all books created messages to RabbitMQ"

    def handle(self, *args, **options):
        books = Book.objects.all()

        publisher = FanoutPublisher(name=os.getenv('BOOKS_EXCHANGE'))

        for book in books:
            serializer = BookSerializer(book)

            publisher.publish(message=AmqpMessage(
                routing_key=os.getenv('BOOKS_CREATED_ROUTING_KEY'),
                body=serializer.data
            ))