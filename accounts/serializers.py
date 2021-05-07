from rest_framework import serializers

from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'phone', 'address', 'gender', 'age', 'description', 'first_name', 'last_name', 'email')

    def validate_password(self, value):
        return make_password(value)
