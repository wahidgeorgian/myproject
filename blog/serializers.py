from django.contrib.auth.models import User
import blog
from blog.models import Post, User
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']



# class PostSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')

#     class Meta:
#         model = Post
#         fields = ['author','title','text','category','tag','thumbnail','feature',]

    

    