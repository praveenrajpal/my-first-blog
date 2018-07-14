from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
class Movie(models.Model):
    director = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    movie_title = models.CharField(max_length=200)
    synopsis = models.TextField()
    started_on = models.DateTimeField(
            default=timezone.now)
    launched_on = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.launched_on = timezone.now()
        self.save()

    def __str__(self):
        return self.movie_title
