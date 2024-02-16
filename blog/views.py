from django.shortcuts import render
from rest_framework import viewsets
from .models import (
    CustomUser,
    Post,
    PostLike,
    PostComment
)
from .serializers import (
    CustomUserSerializer,
    PostSerializer,
    PostCommentSerializer,
    PostLikeSerializer
)
from .permissions import IsAuthorOrReadOnly, IsAdmin
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from django_filters import rest_framework as filters


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdmin]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly, ]
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_fields = ('title', 'author', 'subtitle')


class PostLikeViewSet(viewsets.ModelViewSet):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly, ]


class PostCommentViewSet(viewsets.ModelViewSet):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly, ]
