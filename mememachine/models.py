from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 50)
    email = models.CharField()
    password = models.CharField(max_length = 50)
    pfp = models.CharField()
    liked_posts = models
    posts = models

class Meme(models.Model):
    title = models.CharField(max_length=50)
    caption = model.CharField(max_length=150)
    author = model.CharField(max_length=50)
    image_url = model.CharField(max_length=400)
    meme_id = model.CharField(max_length=50)
    date=models.DateTimeField(auto_now_add=True)
