from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from .models import Book
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User

from .serializers import BookSerializers, UserSerializer

# Create your views here.

def first(request):
    books = Book.objects.all()

    return render(request, 'first.html', {'books': books})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permisson_classes = (AllowAny,)

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializers
    
    authentication_class = TokenAuthentication
   
    queryset = Book.objects.all()
    permisson_classes = (AllowAny,)
