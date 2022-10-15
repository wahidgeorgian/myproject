from dataclasses import field
from blog.models import User, Comment
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password','email','city','state', 'country']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields =['post', 'name', 'email', 'body', 'parent']