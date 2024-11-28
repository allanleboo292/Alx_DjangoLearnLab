# api/test_views.py

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book
from rest_framework.reverse import reverse

class BookAPITests(APITestCase):
    
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.book1 = Book.objects.create(title="Book 1", author="Author 1", publication_year=2021)
        self.book2 = Book.objects.create(title="Book 2", author="Author 2", publication_year=2022)
        self.book3 = Book.objects.create(title="Book 3", author="Author 1", publication_year=2023)
        
        self.url = reverse('book-list')  # Adjust the URL name based on your actual URL naming convention

    def test_book_creation(self):
        
        data = {'title': 'New Book', 'author': 'New Author', 'publication_year': 2024}
        self.client.login(username='testuser', password='password123')
        
        response = self.client.post(self.url, data, format='json')
        
        # Check that the status code is 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Check that the response contains the created book's data
        self.assertEqual(response.data['title'], 'New Book')
        self.assertEqual(response.data['author'], 'New Author')
        self.assertEqual(response.data['publication_year'], 2024)

    def test_book_list(self):
        
        response = self.client.get(self.url, format='json')
        
        # Check that the status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Ensure the response contains both books
        self.assertEqual(len(response.data), 3)  # Adjust based on the number of books created

    def test_book_update(self):
        
        update_data = {'title': 'Updated Book', 'author': 'Updated Author', 'publication_year': 2024}
        url = reverse('book-detail', args=[self.book1.pk])  # Adjust based on your URL configuration
        
        self.client.login(username='testuser', password='password123')
        
        response = self.client.put(url, update_data, format='json')
        
        # Check that the status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Ensure the book's information has been updated
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book')
        self.assertEqual(self.book1.author, 'Updated Author')
        self.assertEqual(self.book1.publication_year, 2024)

    def test_book_delete(self):
        
        url = reverse('book-detail', args=[self.book1.pk])  # Adjust based on your URL configuration
        self.client.login(username='testuser', password='password123')
        
        response = self.client.delete(url, format='json')
        
        # Check that the status code is 204 (No Content), which means deletion was successful
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Ensure the book is actually deleted
        with self.assertRaises(Book.DoesNotExist):
            self.book1.refresh_from_db()

    def test_book_filtering(self):
        
        url = self.url + '?author=Author%201'  # Filter by 'Author 1'
        
        response = self.client.get(url, format='json')
        
        # Check that the status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check that only books by 'Author 1' are returned
        self.assertEqual(len(response.data), 2)  # Should return 'Book 1' and 'Book 3'

    def test_book_search(self):
        
        url = self.url + '?search=Book'  # Search for books with 'Book' in the title
        
        response = self.client.get(url, format='json')
        
        # Check that the status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check that all books in the response contain 'Book' in their title
        for book in response.data:
            self.assertIn('Book', book['title'])

    def test_book_ordering(self):
        
        url = self.url + '?ordering=title'  # Order books by title
        
        response = self.client.get(url, format='json')
        
        # Check that the status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check that the books are ordered by title
        self.assertEqual(response.data[0]['title'], 'Book 1')
        self.assertEqual(response.data[1]['title'], 'Book 2')
        self.assertEqual(response.data[2]['title'], 'Book 3')

    def test_permissions(self):
        
        url = self.url
        
        # Test without logging in (unauthenticated)
        response = self.client.post(url, {'title': 'New Book', 'author': 'Author', 'publication_year': 2024}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        # Test as authenticated user
        self.client.login(username='testuser', password='password123')
        response = self.client.post(url, {'title': 'New Book', 'author': 'Author', 'publication_year': 2024}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

