from dataclasses import field
from blog import models
from blog.models import User, Post, Comment
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password','email','city','state', 'country', 'image',)

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('id','author','title','text')
       


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields =['post', 'name', 'email', 'body']

# author = serializers.ReadOnlyField(source='author.username')

