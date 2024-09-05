import os, json, signal

from django.core.management.base import BaseCommand

from orderAPI.models import Book
from orderAPI.serializers import BookSerializer
from coreApp.services.rabbitmq import Consumer

class Command(BaseCommand):
    help = "Consumes get all book created messages from RabbitMQ"

    def handle(self, *args, **options):
        self.consumer = Consumer(
            callback=self._callback,
            name = f"books_queue_orderAPI",
            exchange=os.getenv('BOOKS_EXCHANGE'),
            routing_key=os.getenv('BOOKS_CREATED_ROUTING_KEY')
        )

        signal.signal(signal.SIGINT, self._stop_gracefully)
        signal.signal(signal.SIGTERM, self._stop_gracefully)

        self.consumer.consume(auto_ack=True)

        print('[Order API] Consumer shutting down...')

    def _callback(self, channel, method, properties, body):
            message = json.loads(body)

            try:
                serializer = BookSerializer(message)
                Book.objects.create(**serializer.data)

                print(f"[Order API] Received {message}")
            except Exception as e:
                print(e)
            finally:
                print("[Order API] Done")

    def _stop_gracefully(self, signum, frame):
        self.consumer.close()

    