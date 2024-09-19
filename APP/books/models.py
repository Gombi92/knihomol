from django.db import models

class Book(models.Model):
    READING_PROGRESS_CHOICES = [
        ('Read', 'Read'),
        ('Unread', 'Unread'),
        ('In progress', 'In progress'),
    ]

    BOOKS_CONDITION_CHOICES = [
        ('a', 'Excellent'),
        ('b', 'Good'),
        ('c', 'Poor'),
    ]

    BOOK_TYPE_CHOICES = [
        ('E-book', 'E-book'),
        ('Physical', 'Physical'),
    ]

    books_name = models.CharField(max_length=150)
    year_of_publication = models.IntegerField(null=True, blank=True)
    reading_progress = models.CharField(max_length=12, choices=READING_PROGRESS_CHOICES, null=True, blank=True)
    books_condition = models.CharField(max_length=1, choices=BOOKS_CONDITION_CHOICES, null=True, blank=True)
    number_of_pages = models.SmallIntegerField(null=True, blank=True)
    language = models.CharField(max_length=50, default='čeština')
    book_type = models.CharField(max_length=8, choices=BOOK_TYPE_CHOICES, null=True, blank=True)

    class Meta:
        db_table = 'books'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.books_name
