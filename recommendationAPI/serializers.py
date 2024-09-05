from rest_framework import serializers

from coreApp.validators import valid_isbn, isbn_length

from .models import User, Book, Recommendation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email"]
        ref_name = "recommendationAPI.UserSerializer"

class BookSerializer(serializers.ModelSerializer):
    isbn = serializers.CharField(max_length=13, help_text='Please supply a 13 digit-long ISBN.', validators=[valid_isbn, isbn_length])

    class Meta:
        model = Book
        fields = ["isbn"]
        ref_name = "recommendationAPI.BookSerializer"

class RecommendationSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(
        slug_field='isbn',
        queryset=Book.objects.all()
     )
    user = serializers.SlugRelatedField(
        slug_field='email',
        queryset=User.objects.all()
     )

    class Meta:
        model = Recommendation
        fields = ["reason", "book", "user"]