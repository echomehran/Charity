from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer
from .models import User

class UserType(APIView):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['post']

    def post(self, request):
        user_type = None
        
        if request.user.is_benefactor:
            user_type = 'benefactor'
        
        if request.user.is_charity:
            user_type = 'charity'
        
        return Response(data={'user_type': user_type})

class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['post']

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class UserRegistration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
