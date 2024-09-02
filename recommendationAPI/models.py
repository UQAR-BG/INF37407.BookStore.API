from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length = 254)

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=13, help_text='Please supply a 13 digit-long ISBN.')

class Recommendation(models.Model):
    id = models.AutoField(primary_key=True)
    recommended_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    recommended_to_user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()