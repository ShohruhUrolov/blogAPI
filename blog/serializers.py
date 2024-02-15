from .models import(
    CustomUser,
    Post,
    PostLike,
    PostComment
)
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email

        return token


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'id', 'first_name', 'last_name', 'username', 'email', 'password'
        ]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id', 'author', 'title', 'subtitle', 'body', 'image', 'create_at',
            'update_at'
        ]


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = [
            'id', 'post', 'author', 'text'
        ]


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = [
            'id', 'post', 'author'
        ]