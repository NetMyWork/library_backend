from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey, ContentType
from django.conf import settings
from django.contrib.auth.models import User
class UserBook(models.Model):
    user: models.ForeignKey = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content_type: models.ForeignKey = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id: models.PositiveIntegerField = models.PositiveIntegerField()
    book: GenericForeignKey = GenericForeignKey('content_type', 'object_id')
    last_read: models.DateTimeField = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.book.title}"