from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length = 50)
    pfp = models.CharField(max_length=100)
    liked_posts = models
    posts = models

class Meme(models.Model):
    title = models.CharField(max_length=50)
    caption = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    image_url = models.CharField(max_length=400)
    meme_id = models.CharField(max_length=50)
    date=models.DateTimeField(auto_now_add=True)
