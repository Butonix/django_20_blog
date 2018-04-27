from django.db import models
from django.urls import reverse


# Create your models here.


def upload_location(instance, filename):
    return '%s/%s' %(instance.id, filename)

class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.FileField(blank=True,null=True,
                             upload_to=upload_location,)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return '%s' % (self.id)
        return reverse('posts:post_detail', kwargs={'id': self.id})