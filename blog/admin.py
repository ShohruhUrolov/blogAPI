from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import (
    Post,
    PostLike,
    PostComment,
    CustomUser
)
# Register your models here.


class PostLikeAdmin(ModelAdmin):
    model = PostLike
    list_display = ['post', 'author']


class PostCommentAdmin(ModelAdmin):
    model = PostComment
    list_display = ['author', 'post', 'text']


class PostAdmin(ModelAdmin):
    model = Post
    list_display = ['author', 'title', 'subtitle', 'body', 'image', 'create_at', 'update_at']


admin.site.register(CustomUser)
admin.site.register(Post, PostAdmin)
admin.site.register(PostLike, PostLikeAdmin)
admin.site.register(PostComment, PostCommentAdmin)
