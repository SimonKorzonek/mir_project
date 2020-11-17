from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    publication_datetime = models.DateTimeField(auto_now_add=True, blank=True)
    online = models.BooleanField(default=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} by {self.author}'