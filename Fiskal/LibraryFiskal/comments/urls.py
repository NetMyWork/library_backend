from django.urls import path
from .views import AddComment

urlpatterns = [
    path('book/<int:book_id>/comment/', AddComment.as_view(), name='add-comment'),
]