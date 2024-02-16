from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    images = models.ImageField(upload_to="images/book", null=True, blank=True)

    def __str__(self):
        return self.name + " " + self.surname


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.CharField(max_length=255)
    year = models.DateField()
    format = models.TextField()
    pages = models.IntegerField()

    def __str__(self):
        return self.title
