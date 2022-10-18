from dataclasses import field
from blog import models
from blog.models import User, Post, Comment, CategoryTable as Category, Tags
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password','email','city','state', 'country', 'image',)

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('id','author','title','text','thumbnail','feature','created_date','published_date','category','tag','slug',)
       
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields =('post', 'name', 'email', 'body')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug',)

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('name', 'slug',)