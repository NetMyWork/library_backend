from django.urls import path, include
from .views import SignUpView, SignInView, check_authenticated
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api-auth/', include('rest_framework.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('check-authenticated/', check_authenticated, name='check'),
    path('signin/', SignInView.as_view(), name='signin'),

]