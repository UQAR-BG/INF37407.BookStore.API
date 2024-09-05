import os, json, signal

from django.core.management.base import BaseCommand

from reviewAPI.models import Book
from reviewAPI.serializers import BookSerializer
from coreApp.services.rabbitmq import Consumer

class Command(BaseCommand):
    help = "Consumes get all book created messages from RabbitMQ"

    def handle(self, *args, **options):
        self.consumer = Consumer(
            callback=self._callback,
            name = f"books_queue_reviewAPI",
            exchange=os.getenv('BOOKS_EXCHANGE'),
            routing_key=os.getenv('BOOKS_DELETED_ROUTING_KEY')
        )

        signal.signal(signal.SIGINT, self._stop_gracefully)
        signal.signal(signal.SIGTERM, self._stop_gracefully)

        self.consumer.consume(auto_ack=True)

        print('[Review API] Consumer shutting down...')

    def _callback(self, channel, method, properties, body):
            message = json.loads(body)

            try:
                serializer = BookSerializer(message)
                book = Book.objects.get(isbn=serializer.data['isbn'])
                book.delete()

                print(f"[Review API] Deleted book: {serializer.data['isbn']}")
            except Exception as e:
                print(e)
            finally:
                print("[Review API] Done")

    def _stop_gracefully(self, signum, frame):
        self.consumer.close()

    