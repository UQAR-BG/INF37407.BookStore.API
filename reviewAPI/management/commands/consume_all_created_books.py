import os, json, uuid

from django.core.management.base import BaseCommand

from reviewAPI.models import Book
from reviewAPI.serializers import BookSerializer
from coreApp.services.rabbitmq import Consumer

class Command(BaseCommand):
    help = "Consumes get all book created messages from RabbitMQ"

    def handle(self, *args, **options):
        consumer = Consumer(
            callback=self._callback,
            name = f"books_queue_{uuid.uuid4()}",
            auto_delete=True,
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