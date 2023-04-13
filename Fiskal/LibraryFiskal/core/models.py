from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from comments.models import Comment
from rate.models import Rate
# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=300)
    def __str__(self):
        return self.tag
class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    publication_date = models.DateField()
    cover_image = models.ImageField(upload_to='covers/', blank=True)
    book=models.FileField(upload_to='book/')
    comments = GenericRelation(Comment)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True,related_name='books')
    ratings = GenericRelation(Rate)
    tip=models.CharField(max_length=100, default='book')
    type=models.CharField(max_length=100, default='book')
    def __str__(self):
        return self.title
class AudioBook(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    publication_date = models.DateField()
    cover_image = models.ImageField(upload_to='covers/', blank=True)
    book=models.FileField(upload_to='Audiobook/')
    comments = GenericRelation(Comment)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True,related_name='abooks')
    ratings = GenericRelation(Rate)
    tip=models.CharField(max_length=100, default='audiobook')
    type=models.CharField(max_length=100, default='audiobook')
    def __str__(self):
        return self.title
class Article(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True)
    publication_date = models.DateField()
    cover_image = models.ImageField(upload_to='covers/', blank=True)
    book=models.FileField(upload_to='Article/',null=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True,related_name='article')
    ratings = GenericRelation(Rate)
    tip=models.CharField(max_length=100, default='article')
    type=models.CharField(max_length=100, default='article')
    def __str__(self):
        return self.title
class Work(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    publication_date = models.DateField()
    cover_image = models.ImageField(upload_to='covers/', blank=True)
    book=models.FileField(upload_to='Work/')
    comments = GenericRelation(Comment)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True,related_name='work')
    ratings = GenericRelation(Rate)
    tip=models.CharField(max_length=100, default='work')
    type=models.CharField(max_length=100, default='work')
    def __str__(self):
        return self.title
class Event(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    publication_date = models.DateField()
    cover_image = models.ImageField(upload_to='events/', blank=True)
    cover_video = models.FileField(upload_to='events/', blank=True)
    tip=models.CharField(max_length=100, default='event')
    def __str__(self):
        return self.title
