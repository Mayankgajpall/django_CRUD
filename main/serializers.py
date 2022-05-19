from dataclasses import field
from rest_framework import serializers
from main.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'description', 'language', 'price']