from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=150)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author,on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=15, unique=True)
    category = models.CharField(max_length=20)
    available_status = models.BooleanField(default=True)

    def __str__(self):
        return self.title