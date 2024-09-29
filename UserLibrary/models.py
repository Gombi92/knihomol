from django.db import models
from django.contrib.auth.models import User
from RegisteredBooks.models import RegisteredBooks  # Importování modelu RegisteredBooks

class UserLibrary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(RegisteredBooks, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"