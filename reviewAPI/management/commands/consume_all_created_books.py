import os, json

from django.core.management.base import BaseCommand

from orderAPI.models import Book
from orderAPI.serializers import BookSerializer
from coreApp.services.rabbitmq import FastConsumer

class Command(BaseCommand):
    help = "Consumes get all book created messages from RabbitMQ"

    def handle(self, *args, **options):
        consumer = FastConsumer(
            callback=self._callback,
            name=os.getenv('BOOKS_QUEUE'),
            exchange=os.getenv('BOOKS_EXCHANGE'),
            routing_key=os.getenv('BOOKS_CREATED_ROUTING_KEY')
        )

        consumer.consume(auto_ack=True)

        print('Consumer shutting down...')

    def _callback(self, channel, method, properties, body):
        message = json.loads(body)
        print(f" [x] Received {message}")

        serializer = BookSerializer(message)
        book = Book.objects.create(**serializer.data)
        book.save()

        print(" [x] Done")