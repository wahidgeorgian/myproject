from urllib import request
from blog.models import User, Post, Comment, CategoryTable as Category, Tags
from blog.api.serializers import UserSerializer, PostSerializer, CommentSerializer, CategorySerializer,TagsSerializer
from rest_framework import viewsets, status
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny 


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
  

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    Http_mathod_names = ['get',]
    def get_queryset(self):
        return Post.objects.all()
    

class PostDetail(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    Http_mathod_name = ['get',]
    def get_queryset(self):
        return Post.objects.all()

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    Http_mathod_name = ['get',]

    def get_queryset(self):
        return Comment.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    Http_method_name = ['get',]

    def get_queryset(self):
        return Category.objects.all()

class TagsViewSet(viewsets.ModelViewSet):
    serializer_class = TagsSerializer
    Http_method_name = ['get',]
    
    def get_queryset(self):
        return Tags.objects.all()

