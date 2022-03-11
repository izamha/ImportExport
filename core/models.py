from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=450)
    liked = models.ManyToManyField(User, related_name='liked')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post {self.pk}'

    @property
    def comments(self):
        return self.comment_set.all()



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment {self.pk}'

