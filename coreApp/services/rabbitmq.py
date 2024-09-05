from pika.exchange_type import ExchangeType
from pika import BlockingConnection, PlainCredentials, ConnectionParameters, BasicProperties
import json, os, pika, threading

class AmqpConfig:
    def __init__(self, name='', exchange='', routing_key='', durable=False, exclusive=False, auto_delete=False, arguments=None):
        self.name = name
        self.exchange = exchange
        self.routing_key = routing_key
        self.durable = durable
        self.exclusive = exclusive
        self.auto_delete = auto_delete
        self.arguments = arguments

class AmqpExchangeConfig(AmqpConfig):
    def __init__(self, name='', type=ExchangeType.direct, durable=False, internal=False, auto_delete=False, arguments=None):
        self.type = type
        self.internal = internal
        super().__init__(name, '', '', durable, False, auto_delete, arguments)

class AmqpMessage():
    def __init__(self, routing_key, body, properties: BasicProperties=None, mandatory=False):
        self.routing_key = routing_key
        self.body = body
        self.properties = properties
        self.mandatory = mandatory

credentials = PlainCredentials(
    username=os.getenv('RABBITMQ_DEFAULT_USER'),
    password=os.getenv('RABBITMQ_DEFAULT_PASS')
)

params = ConnectionParameters(
    host=os.getenv('RABBITMQ_HOST'), 
    port=os.getenv('RABBITMQ_PORT'),
    credentials=credentials,
    heartbeat=0
)

class AmqpClient():
    def close(self):
        self._channel.close()
        self._connection.close()

    def _init_connection(self, parameters: ConnectionParameters):
        self._connection = BlockingConnection(parameters)

    def _init_channel(self, connection: BlockingConnection):
        self._channel = connection.channel()

class LongRunningAmqpClient(AmqpClient, threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.daemon = True
        self.is_running = True
        
        self._init_connection(params)
        self._connection.add_on_connection_blocked_callback(self.__on_blocked_callback)

        self._init_channel(self._connection)

    def run(self):
        while self.is_running:
            self._connection.process_data_events()

    def stop(self):
        print("Stopping...")
        self.is_running = False
        # Wait until all the data events have been processed
        self._connection.process_data_events(time_limit=1)
        if self._connection.is_open:
            self._connection.close()
        print("Stopped")

    def __on_blocked_callback(self, connection: BlockingConnection, method_frame):
        print("Connection is blocked. Sending a heartbeat to keep the connection alive.")
        connection.process_data_events()

class Publisher(LongRunningAmqpClient):
    def __init__(self, config=AmqpExchangeConfig()):
        super().__init__()
        self.__init_exchange(config)
        self._config = config

    def publish(self, message):
        self._connection.add_callback_threadsafe(lambda: self._publish(message))

    def _publish(self, message: AmqpMessage):
        self._channel.basic_publish(
            exchange=self._config.name, 
            routing_key=message.routing_key, 
            body=json.dumps(message.body),
            properties=message.properties)

    def __init_exchange(self, config=AmqpExchangeConfig()):
        self._exchange = self._channel.exchange_declare(
            exchange=config.name,
            exchange_type=config.type,
            durable=config.durable,
            auto_delete=config.auto_delete,
            internal=config.internal,
            arguments=config.arguments
        )

class DirectPublisher(Publisher):
    def __init__(self, name='', durable=False, internal=False, auto_delete=False, arguments=None):
        super().__init__(AmqpExchangeConfig(
            name=name,
            type=ExchangeType.direct,
            durable=durable,
            internal=internal,
            auto_delete=auto_delete,
            arguments=arguments
        ))

class FastPublisher(DirectPublisher):
    def __init__(self, name='', internal=False, auto_delete=False, arguments=None):
        super().__init__(
            name=name,
            durable=False,
            internal=internal,
            auto_delete=auto_delete,
            arguments=arguments
        )

class FanoutPublisher(Publisher):
    def __init__(self, name='', durable=False, internal=False, auto_delete=False, arguments=None):
        super().__init__(AmqpExchangeConfig(
            name=name,
            type=ExchangeType.fanout,
            durable=durable,
            internal=internal,
            auto_delete=auto_delete,
            arguments=arguments
        ))
        
class BaseConsumer(AmqpClient):
    def __init__(self, on_message_callback, config=AmqpConfig()):
        self._config = config
        self._on_message_callback = on_message_callback

        self._init_connection(params)
        self._init_channel(self._connection)
        self.__init_queue()
        self.__bind_queue()

    def consume(self, auto_ack=False, exclusive=False, consumer_tag=None, arguments=None):
        self._channel.basic_consume(
            queue=self._config.name,
            on_message_callback=self._on_message_callback,
            auto_ack=auto_ack,
            exclusive=exclusive,
            consumer_tag=consumer_tag,
            arguments=arguments
        )

        print('Consumer is listening for messages...')
        self._channel.start_consuming()

    def __init_queue(self):
        self._queue = self._channel.queue_declare(
            queue=self._config.name,
            durable=self._config.durable,
            exclusive=self._config.exclusive,
            auto_delete=self._config.auto_delete,
            arguments=self._config.arguments
        )

    def __bind_queue(self):
        self._channel.queue_bind(
            queue=self._queue.method.queue,
            exchange=self._config.exchange,
            routing_key=self._config.routing_key
        )

class Consumer(BaseConsumer):
    def __init__(self, callback, name='', exchange='', routing_key='', exclusive=False, auto_delete=False):
        super().__init__(
            on_message_callback=callback,
            config=AmqpConfig(
                name=name,
                exchange=exchange,
                routing_key=routing_key,
                durable=True,
                exclusive=exclusive,
                auto_delete=auto_delete,
                arguments={"x-queue-type": "quorum"}
            ))