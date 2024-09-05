from rest_framework import serializers

from coreApp.validators import valid_isbn, isbn_length

from .models import Book

class BookSerializer(serializers.ModelSerializer):
    isbn = serializers.CharField(max_length=13, help_text='Please supply a 13 digit-long ISBN.', validators=[valid_isbn, isbn_length])

    class Meta:
        model = Book
        fields = ["title", "author", "description", "isbn", "price", "stock", "published_date", "genre"]
        ref_name = "bookAPI.BookSerializer"