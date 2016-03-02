from django.db import models

# Create your models here.

class Bookmark(models.Model):
    original_url = models.URLField()
    title = models.CharField(max_length=30)
    description = models.TextField()
    shortened_url = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def click_count(self):
        return self.click_set.all().count()

    def __str__(self):
        return self.shortened_url

    class Meta:
        ordering = ['-timestamp']

class Click(models.Model):
    clicked = models.BooleanField(default=True)
    url = models.ForeignKey(Bookmark)


