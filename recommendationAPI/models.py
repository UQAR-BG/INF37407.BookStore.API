from django.db import models
from rest_framework.serializers import ValidationError

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length = 254)

    def __str__(self):
        return self.email

    using = 'recommendations'

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=13, help_text='Please supply a 13 digit-long ISBN.', unique=True)

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

    using = 'recommendations'

class Recommendation(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()

    using = 'recommendations'