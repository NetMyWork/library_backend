from django.db import models
from django.conf import settings
from core.models import Book
from django.contrib.auth.models import User

class Recommendation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} recommends {self.book.title}'
