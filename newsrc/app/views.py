from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from .models import Book
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from .serializers import BookSerializers

# Create your views here.

def first(request):
    books = Book.objects.all()

    return render(request, 'first.html', {'books': books})

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializers
    authentication_class = TokenAuthentication
    queryset = Book.objects.all()
