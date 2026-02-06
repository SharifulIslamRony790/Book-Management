from django.test import TestCase, Client
from django.urls import reverse
from .models import Book
import datetime

class BookModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            name="Test Book",
            journal="Test Journal",
            author="Test Author",
            published_date=datetime.date(2023, 1, 1),
            description="Test Description",
            publisher="Test Publisher"
        )

    def test_book_creation(self):
        self.assertEqual(self.book.name, "Test Book")
        self.assertEqual(str(self.book), "Test Book")

class BookViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.book = Book.objects.create(
            name="Test Book",
            journal="Test Journal",
            author="Test Author",
            published_date=datetime.date(2023, 1, 1),
            description="Test Description",
            publisher="Test Publisher"
        )
        self.list_url = reverse('book_list')
        self.create_url = reverse('book_create')
        self.detail_url = reverse('book_detail', args=[self.book.pk])
        self.update_url = reverse('book_update', args=[self.book.pk])
        self.delete_url = reverse('book_delete', args=[self.book.pk])

    def test_book_list_view(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Book")
        self.assertTemplateUsed(response, 'index.html')

    def test_book_detail_view(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Description")
        self.assertTemplateUsed(response, 'details.html')

    def test_book_create_view(self):
        response = self.client.post(self.create_url, {
            'name': 'New Book',
            'journal': 'New Journal',
            'author': 'New Author',
            'published_date': '2024-01-01',
            'description': 'New Description',
            'publisher': 'New Publisher'
        })
        self.assertEqual(response.status_code, 302) # Redirects after success
        self.assertEqual(Book.objects.count(), 2)

    def test_book_update_view(self):
        response = self.client.post(self.update_url, {
            'name': 'Updated Book',
            'journal': 'Test Journal',
            'author': 'Test Author',
            'published_date': '2023-01-01',
            'description': 'Test Description',
            'publisher': 'Test Publisher'
        })
        self.assertEqual(response.status_code, 302)
        self.book.refresh_from_db()
        self.assertEqual(self.book.name, 'Updated Book')

    def test_book_delete_view(self):
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Book.objects.count(), 0)
