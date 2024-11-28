from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Includes custom validation to ensure the publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Dynamically nests BookSerializer for related books.
    """
    books = BookSerializer(many=True, read_only=True)  # Ensures the relationship is serialized dynamically.

    class Meta:
        model = Author
        fields = ['name', 'books']  # Includes the author's name and their books.
