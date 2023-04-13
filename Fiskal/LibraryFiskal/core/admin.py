from django.contrib import admin
from .models import Book,AudioBook,Article,Work,Event,Tag
# Register your models here.
admin.site.register(Book)
admin.site.register(AudioBook)
admin.site.register(Article)
admin.site.register(Work)
admin.site.register(Event)
admin.site.register(Tag)

