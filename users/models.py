from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user        = models.ForeignKey(User)
    username    = models.CharField(max_length=30)

class Rating(models.Model):
    user        = models.ForeignKey(UserProfile)
    book        = models.ForeignKey("booktalk.Book")
    rating      = models.IntegerField()

class Opinion(models.Model):
    user        = models.ForeignKey(UserProfile)
    segment     = models.ForeignKey("booktalk.Segment")
    opinion     = models.TextField()

class OpinionComment(models.Model):
    user        = models.ForeignKey(UserProfile)
    opinion     = models.ForeignKey(Opinion)
    comment     = models.CharField(max_length=300)
