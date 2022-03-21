from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse(
            "blog:detail", kwargs={"slug": self.slug}
        )  # "detail" foi definido no urls.py, esse metodo reverse esta definindo URL de um post
