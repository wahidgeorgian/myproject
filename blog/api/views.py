from urllib import request
from blog.models import User, Post, Comment
from blog.api.serializers import UserSerializer, PostSerializer, CommentSerializer
from rest_framework import viewsets, status
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny 


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
  

class PostViewSet(viewsets.ModelViewSet):
    
    querset = Post.objects.all()
    serializer_class = PostSerializer
    Http_mathod_names = ['get',]
    def get_queryset(self):
        return Post.objects.all()

    # Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


    # def get_queryset(self):
    #     return HttpResponse(status=404)
    
    

class PostDetail(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return

