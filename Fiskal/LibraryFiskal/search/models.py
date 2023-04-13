from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='book_images/')

    def __str__(self):
        return self.title
