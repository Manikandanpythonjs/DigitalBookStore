from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.


class Authors(models.Model):

    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.name


class Book(models.Model):

    BookReferenceId = models.UUIDField(default=uuid.uuid4, editable=False)
    BookTitle = models.CharField(max_length=50)
    PageCount = models.IntegerField(default=0)
    Description = models.TextField(null=True)
    ImageUrl = models.CharField(max_length=250, null=True)
    AuthorName = models.ManyToManyField(Authors)

    def __str__(self):
        return f"{self.id} {self.BookTitle}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    ReviewComment = models.TextField()
    book_ref = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.id} {self.ReviewComment}"
