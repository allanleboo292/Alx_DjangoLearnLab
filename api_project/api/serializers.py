from rest_framework import serializer
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        field = '__all__'
        