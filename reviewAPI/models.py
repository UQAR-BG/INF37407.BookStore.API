from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length = 254)

    using = 'reviews'

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=13, help_text='Please supply a 13 digit-long ISBN.')

    using = 'reviews'

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    book_reviewed = models.ForeignKey(Book, on_delete=models.CASCADE)
    written_by_user = models.ForeignKey(User, on_delete=models.CASCADE)

    using = 'reviews'