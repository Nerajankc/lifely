from django.db import models
# from django.contrib.auth.models import Heading

# Create your models here.


class Aboutus(models.Model):
    heading = models.CharField(max_length=20, null=True)
    date = models.DateField(null=True)
    body = models.TextField(null=True)
    midbody = models.TextField(null=True)
    lastbody = models.TextField(null=True)


class FeedBacks(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.email


class NewsLetter(models.Model):
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.email


class Gallery(models.Model):
    name = models.CharField(max_length=200, blank=True)
    image = models.ImageField(null=True, blank=True, default='/sample.jpeg')

    def __str__(self):
        return self.name
