from django.db import models

# Create your models here.
class Recommendation(models.Model):
    id = models.AutoField(primary_key=True)
    recommended_book = models.ForeignKey("Book", on_delete=models.CASCADE)
    recommended_to_user = models.ForeignKey("User", on_delete=models.CASCADE)
    reason = models.TextField()