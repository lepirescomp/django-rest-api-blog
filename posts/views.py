from django.shortcuts import render
from rest_framework import generics
# Create your views here.

from .models import Post
from .serializers import PostSerializers

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
