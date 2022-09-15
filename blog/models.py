from unicodedata import category
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django_extensions.db.fields import AutoSlugField
from django.contrib import admin

# Model for category table.....
class CategoryTable(models.Model):
    
    name =models.CharField(max_length=250)
    slug = AutoSlugField(populate_from = 'name' ,unique=True)

    def __str__(self):
        return self.name

# Model for tags.......
class Tags(models.Model):

    name =models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='name',unique=True)

    def __str__(self):
        return self.name

# Model for Post.....
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(null=True,blank=True)
    thumbnail = models.ImageField(upload_to='thumbnail/')
    feature = models.ImageField(upload_to ='feature/')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(CategoryTable,on_delete=models.CASCADE)
    tag =models.ManyToManyField(Tags)
    slug = AutoSlugField(populate_from='title' ,unique=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    

    def get_image(self):
        return self.image

    

class User(AbstractUser):
    username =models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length = 200)
    mobile_number = models.CharField(max_length=12)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=25)
    country = models.CharField(max_length=20)
    image = models.ImageField(upload_to='user_image')

    def get_image(self):
        return self.image

    def __str__(self):
        return self.email

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    body = models.TextField(null=True,blank=True)
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete= models.CASCADE ,related_name='replies')

    class meta:
        ordering = ('created')

    def __str__(self):
        return 'Comment by {}'.format(self.name)
