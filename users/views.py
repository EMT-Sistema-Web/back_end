from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return UserUpdateSerializer
        return UserSerializer
    
    def list(self, request, *args, **kwargs):
        if not request.user.is_superuser and request.user.user_type != 1:
            queryset = CustomUser.objects.filter(id=request.user.id)
        else:
            queryset = self.filter_queryset(self.get_queryset())
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)