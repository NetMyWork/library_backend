from django.urls import path
from .views import AddReview

urlpatterns = [
    path('book/<int:book_id>/review/', AddReview.as_view(), name='add-review'),
]