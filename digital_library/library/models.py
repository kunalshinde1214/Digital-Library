from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    LANGUAGE_CHOICES = [
        ('EN', 'English'),
        ('SA', 'Sanskrit'),
        ('MR', 'Marathi'),
        ('DE', 'German'),
        ('CO', 'Computer'),
        ('OTHER', 'Other'),
    ]

    GENRE_CHOICES = [
        ('FICTION', 'Fiction'),
        ('NONFICTION', 'Non-Fiction'),
        ('SCIENCE', 'Science'),
        ('TECH', 'Technology'),
        ('BUSINESS', 'Business'),
        ('MYSTERY', 'Mystery'),
        ('ROMANCE', 'Romance'),
        ('SCIFI', 'Science Fiction'),
        ('FANTASY', 'Fantasy'),
        ('HORROR', 'Horror'),
        ('BIOGRAPHY', 'Biography'),
        ('HISTORY', 'History'),
        ('POETRY', 'Poetry'),
        ('DRAMA', 'Drama'),
        ('OTHER', 'Other'),
    ]

    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, default='FICTION')
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='EN')
    release_date = models.DateField()
    summary = models.TextField()
    file = models.FileField(upload_to='books/')
    file_type = models.CharField(max_length=10)
    upload_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} by {self.author.name}"

    class Meta:
        ordering = ['-upload_date']