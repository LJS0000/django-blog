from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies'
    )

    def __str__(self):
        return self.content


class Hashtag(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=10)

    def __str__(self):
        return self.content
