from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=1200)
    image = models.ImageField(upload_to='post_images')