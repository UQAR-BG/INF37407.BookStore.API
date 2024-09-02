from django.db import models

# Create your models here.
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    rating = models.IntegerField(max_length=5)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    book_reviewed = models.ForeignKey("Book", on_delete=models.CASCADE)
    written_by_user = models.ForeignKey("User", on_delete=models.CASCADE)