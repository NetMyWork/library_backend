from django.urls import path
from .views import BestRatedAPIView,BestAudioBookView,EventView,ArticleView,WorkView,BookidView,audioid,eventid,articleid,workid,Tagname,ATagname,WTagname,ArTagname,CreateRateView, Search

urlpatterns = [
    path('books/', BestRatedAPIView.as_view(), name='books'),
    path('audiobooks/', BestAudioBookView.as_view(), name='audiobooks'),
    path('events/', EventView.as_view(), name='events'),
    path('article/', ArticleView.as_view(), name='articles'),
    path('work/', WorkView.as_view(), name='work'),
    path('books/<str:pk>', BookidView.as_view(), name='bookid'),
    path('audiobooks/<str:pk>', audioid.as_view(), name='audibooksid'),
    path('events/<str:pk>', eventid.as_view(), name='eventid'),
    path('article/<str:pk>', articleid.as_view(), name='articleid'),
    path('work/<str:pk>', workid.as_view(), name='books'),
    path('books/tag/<str:pk>', Tagname.as_view(), name='books'),
    path('audiobooks/tag/<str:pk>', ATagname.as_view(), name='abookstag'),
    path('work/tag/<str:pk>', WTagname.as_view(), name='wtag'),
    path('article/tag/<str:pk>', ArTagname.as_view(), name='artag'),
    path('rates/create/', CreateRateView.as_view(), name='create_rate'),
    path('search/<str:pk>', Search.as_view()),
]