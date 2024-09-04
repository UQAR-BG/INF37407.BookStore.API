from django.db import models
from rest_framework.serializers import ValidationError

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length = 254)

    def __str__(self):
        return self.email

    using = 'reviews'

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=13, help_text='Please supply a 13 digit-long ISBN.')

    def validate_unique_isbn(self, exclude=None):
        if (
            Book.objects
            .exclude(id=self.id)
            .filter(isbn=self.isbn)
            .exists()
        ):
            raise ValidationError({ 'isbn': ['ISBN must be unique per book.',]})

    def save(self, *args, **kwargs):
        self.validate_unique_isbn()    
        super().save(*args, **kwargs)

    using = 'reviews'

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    using = 'reviews'