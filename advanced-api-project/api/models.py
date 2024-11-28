from django.db import models

# Author model: Represents authors in the system.
# Fields:
# - name: The name of the author.
# Relationship:
# - One-to-Many: An author can write multiple books.
class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
# Book model: Represents books in the system.
# Fields:
# - title: The title of the book.
# - publication_year: The year the book was published.
# - author: Foreign key linking the book to an author.
# Relationship:
# - Many-to-One: Each book is written by one author
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    def __str__(self):
        return self.title
