from rest_framework import serializers
import re


from .models import User, Order, Book, BookLine

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email"]

def valid_isbn(value):
    regex = "^(?=(?:[^0-9]*[0-9]){10}(?:(?:[^0-9]*[0-9]){3})?$)[\\d-]+$"
    p = re.compile(regex)
    if not (re.search(p, value)):
        raise serializers.ValidationError('Le code ISBN ne peut contenir que des chiffres et des tirets.')
    
def isbn_length(value):
    if (len(value) != 13):
        raise serializers.ValidationError('Le code ISBN doit faire 13 chiffres de long.')

class BookSerializer(serializers.ModelSerializer):
    isbn = serializers.CharField(max_length=13, help_text='Please supply a 13 digit-long ISBN.', validators=[valid_isbn, isbn_length])

    class Meta:
        model = Book
        fields = ["isbn", "price", "stock"]

class CompactBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["isbn"]
        extra_kwargs = {
            'isbn': {'validators': [valid_isbn, isbn_length]},
        }

class BookLineSerializer(serializers.ModelSerializer):
    book = CompactBookSerializer()

    class Meta:
        model = BookLine
        fields = ["quantity", "price", "book"]

class OrderSerializer(serializers.ModelSerializer):
    books = BookLineSerializer(many=True, source='bookline_set')
    user = serializers.SlugRelatedField(
        slug_field='email',
        queryset=User.objects.all()
     )

    class Meta:
        model = Order
        fields = ["status", "order_date", "total_price", "books", "user"]
        read_only_fields = ['total_price', "order_date"]

    def create(self, validated_data):
        books_data = validated_data.pop('bookline_set')

        order = Order.objects.create(**validated_data)

        total_price = 0
        for book_data in books_data:
            book = Book.objects.get(isbn=book_data['book']['isbn'])
            book_line = BookLine.objects.create(
                order=order,
                book=book,
                quantity=book_data['quantity'],
                price=book_data['price']
            )
            total_price += book_line.quantity * book_line.price

        order.total_price = total_price
        order.save()
        return order