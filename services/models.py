from django.db import models

# Create your models here.

class Review(models.Model):
    user_email = models.EmailField(max_length=200, blank=True, unique=True)
    review_content = models.TextField()

    def __str__(self):
        return self.user_email