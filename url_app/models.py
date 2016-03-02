from django.contrib.auth.models import User
from django.db import models



class Bookmark(models.Model):
    original_url = models.URLField()
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    shortened_url = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def click_count(self):
        return self.click_set.all().count()

    def __str__(self):
        return '{} {}'.format(self.shortened_url, self.user)

    class Meta:
        ordering = ['-timestamp']

class Click(models.Model):
    clicked = models.BooleanField(default=True)
    url = models.ForeignKey(Bookmark)



