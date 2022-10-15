from dataclasses import field
from blog.models import User, Comment, Post
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password','email','city','state', 'country']

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ['id','author', 'title']

# class UserSerializer(serializers.ModelSerializer):
#     posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'posts']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields =['post', 'name', 'email', 'body']