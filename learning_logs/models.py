from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Topic(models.Model):
    """
    用户学习主题
    """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.text

class Entry(models.Model):
    """
    学到的有关某个主题的具体知识
    """
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50]+'...'