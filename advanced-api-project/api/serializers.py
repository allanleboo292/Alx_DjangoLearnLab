from rest_framework import serializers
from datetime import datetime
from .models import Book, Author

# BookSerializer to serialize all fields of the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields from the Book model

    # Custom validation for the publication_year field
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# AuthorSerializer with nested BookSerializer
class AuthorSerializer(serializers.ModelSerializer):
    # Nested BookSerializer for related books
    books = BookSerializer(many=True, read_only=True, source='book_set')

    class Meta:
        model = Author
        fields = ['name', 'books']  # Include name and related books
