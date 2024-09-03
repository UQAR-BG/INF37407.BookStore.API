from rest_framework import serializers

from coreApp.validators import valid_isbn, isbn_length

from .models import User, Book, Review

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email"]
        ref_name = "reviewAPI.UserSerializer"

class BookSerializer(serializers.ModelSerializer):
    isbn = serializers.CharField(max_length=13, help_text='Please supply a 13 digit-long ISBN.', validators=[valid_isbn, isbn_length])

    class Meta:
        model = Book
        fields = ["isbn"]
        ref_name = "reviewAPI.BookSerializer"

class ReviewSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(
        slug_field='isbn',
        queryset=Book.objects.all()
     )
    user = serializers.SlugRelatedField(
        slug_field='email',
        queryset=User.objects.all()
     )

    class Meta:
        model = Review
        fields = ["rating", "comment", "created_at", "book", "user"]
        read_only_fields = ["created_at"]