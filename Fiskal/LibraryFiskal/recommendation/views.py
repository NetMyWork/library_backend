from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from .models import Recommendation

class RecommendBook(View):
    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        Recommendation.objects.create(user=request.user, book=book)
        messages.success(request, f'You have recommended {book.title} to your friends.')
        return redirect(reverse('book-detail', kwargs={'pk': book_id}))