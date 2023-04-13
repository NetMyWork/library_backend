from django.views.generic import View
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from .models import Rate
from core.models import Book

class AddRate(View):
    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        rating = int(request.POST.get('rating'))
        Rate.objects.create(user=request.user, book=book, rating=rating)
        messages.success(request, f'You have rated {book.title} {rating} stars.')
        return redirect(reverse('book-detail', kwargs={'pk': book_id}))
