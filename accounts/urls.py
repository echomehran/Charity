from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import UserRegistration, LogoutAPIView, UserType

urlpatterns = [
    path('login/', view=obtain_auth_token),
    path('logout/', LogoutAPIView.as_view()),
    path('register/', UserRegistration.as_view()),
    path('usertype/', UserType.as_view()),
]
