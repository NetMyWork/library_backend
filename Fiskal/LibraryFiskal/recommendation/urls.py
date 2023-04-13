from django.urls import path
from .views import RecommendBook

urlpatterns = [
    path('book/<int:book_id>/recommend/', RecommendBook.as_view(), name='recommend-book'),
]