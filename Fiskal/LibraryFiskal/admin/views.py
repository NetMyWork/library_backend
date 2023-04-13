from django.views.generic import View
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from .models import Review

class AddReview(View):
    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        text = request.POST.get('text')
        Review.objects.create(user=request.user, book=book, text=text)
        messages.success(request, f'You have added a review for {book.title}.')
        return redirect(reverse('book-detail', kwargs={'pk': book_id}))