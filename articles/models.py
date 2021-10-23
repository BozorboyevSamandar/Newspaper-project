from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='media/',null=True,blank=True)  #new
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('article_detail',args=[
            str(self.id)])

class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments',
        )
    comment = models.CharField(max_length=120)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
                               )
    def __str__(self):
        return self.comment
    def get_absolute_url(self):
        return reverse('article_list')

