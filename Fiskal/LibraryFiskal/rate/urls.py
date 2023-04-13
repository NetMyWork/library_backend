from django.urls import path
from .views import AddRate

urlpatterns = [
    path('book/<int:book_id>/rate/', AddRate.as_view(), name='add-rate'),
]