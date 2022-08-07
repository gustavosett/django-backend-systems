from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        new_user = User.objects.filter(login=self.request.data.get("login"))
        new_user.password = make_password(self.request.data.get("password"), None, 'md5')
        serializer.save(password=new_user.password)