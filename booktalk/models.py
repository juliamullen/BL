from django.db import models
from users.models import UserProfile


class Book(models.Model):
    title       = models.TextField()
    isbn        = models.IntegerField()
    chapters    = models.IntegerField()

class Segment(models.Model):
    book        = models.ForeignKey(Book)
    chapter     = models.IntegerField()

class Post(models.Model):
    user        = models.ForeignKey(UserProfile)
    text        = models.TextField()
    segment     = models.ForeignKey(Segment)
