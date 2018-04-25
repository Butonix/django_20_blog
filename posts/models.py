from django.db import models
from django.urls import reverse


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return '%s' % (self.id)
        return reverse('posts:post_detail', kwargs={'id': self.id})