from itertools import chain
from django.db.models import F, Q
from rest_framework import generics
from .serializers import BookSerializer, AudioBookSerializer,ArticleSerializer,WorkSerializer,EventSerializer,TagSerializer
from core.models import Book, AudioBook, Article, Work, Event,Tag
from django.db.models import Q
class BestRatedAPIView(generics.ListAPIView):
    """
    API endpoint to retrieve best rated books, audiobooks, articles, and works
    """
    def get_queryset(self):
        top_books = Book.objects.all().order_by('-id')

        # Combine the top-rated objects in a list
        top_rated = list(top_books)
        return top_rated

    serializer_class = BookSerializer
class BestAudioBookView(generics.ListAPIView):
    def get_queryset(self):
        top_books = AudioBook.objects.all().order_by('-id')

        # Combine the top-rated objects in a list
        top_rated = list(top_books)
        return top_rated

    serializer_class = AudioBookSerializer
class EventView(generics.ListAPIView):
    
    def get_queryset(self):
        top_books = Event.objects.all().order_by('-id')

        # Combine the top-rated objects in a list
        top_rated = list(top_books)
        return top_rated

    serializer_class = EventSerializer
class ArticleView(generics.ListAPIView):
    def get_queryset(self):
        top_books = Article.objects.all().order_by('-id')

        # Combine the top-rated objects in a list
        top_rated = list(top_books)
        return top_rated

    serializer_class = ArticleSerializer
class WorkView(generics.ListAPIView):
    def get_queryset(self):
        top_books = Work.objects.all().order_by('-id')

        # Combine the top-rated objects in a list
        top_rated = list(top_books)
        return top_rated

    serializer_class = WorkSerializer
class BookidView(generics.ListAPIView):
    serializer_class = BookSerializer
    
    def get_queryset(self):
        book = Book.objects.filter(id=self.kwargs['pk'])
        return book
class audioid(generics.RetrieveAPIView):
    serializer_class = AudioBookSerializer
    
    def get_queryset(self):
        book = AudioBook.objects.filter(id=self.kwargs['pk'])
        return book

class eventid(generics.ListAPIView):
    serializer_class = EventSerializer
    def get_queryset(self):
        book = Event.objects.filter(id=self.kwargs['pk'])
        return list(book)
class articleid(generics.ListAPIView):
    serializer_class = ArticleSerializer
    def get_queryset(self):
        book = Article.objects.filter(id=self.kwargs['pk'])
        return list(book)
class workid(generics.ListAPIView):
    serializer_class = WorkSerializer
    def get_queryset(self):
        book = Work.objects.filter(id=self.kwargs['pk'])
        return list(book)

class Tagname(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        tag = Tag.objects.get(id=self.kwargs['pk'])
        queryset1 = Book.objects.filter(tag=tag)
        q2=AudioBook.objects.filter(tag=tag)
        q3=Work.objects.filter(tag=tag)
        q4=Article.objects.filter(tag=tag)
        books=queryset1.union(q2.union(q3.union(q4)))
        
        return list(books)
class ATagname(generics.ListAPIView):
    serializer_class = AudioBookSerializer

    def get_queryset(self):
        tag = Tag.objects.get(id=self.kwargs['pk'])
        queryset1 = AudioBook.objects.filter(tag=tag).order_by('-id')
        books=[]
        return queryset1
class ArTagname(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        tag = Tag.objects.get(id=self.kwargs['pk'])
        queryset1 = Article.objects.filter(tag=tag).order_by('-id')
        books=[]
        return queryset1

class WTagname(generics.ListAPIView):
    serializer_class = WorkSerializer

    def get_queryset(self):
        tag = Tag.objects.get(id=self.kwargs['pk'])
        queryset1 = Work.objects.filter(tag=tag).order_by('-id')
        books=[]
        return queryset1



from rest_framework import generics
from .serializers import RateSerializer

class CreateRateView(generics.CreateAPIView):
    serializer_class = RateSerializer
class Search(generics.ListAPIView):
    serializer_class = BookSerializer
    
    def get_queryset(self):
        if self.kwargs['pk'] != 'all':
            book1 = Book.objects.all()
            audio = AudioBook.objects.all()
            work = Work.objects.all()
            article = Article.objects.all()
            book2 = book1.union(audio.union(work.union(article)))
            book=[]
            for i in  book2:
                if self.kwargs['pk'].lower() in i.description.lower():
                    book.append(i)
                elif self.kwargs['pk'].lower() in i.tag.tag.lower():
                    book.append(i)
                elif self.kwargs['pk'].lower() in i.title.lower():
                    book.append(i)
                elif self.kwargs['pk'].lower() in i.author.lower():
                    book.append(i)
        else:
            book1 = Book.objects.all()
            audio = AudioBook.objects.all()
            work = Work.objects.all()
            article = Article.objects.all()
            book = book1.union(audio.union(work.union(article)))
        return book
            