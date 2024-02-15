from .views import (
    CustomUserViewSet,
    PostViewSet,
    PostLikeViewSet,
    PostCommentViewSet
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from rest_framework import routers


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]


router = routers.DefaultRouter()

router.register('users', CustomUserViewSet)
router.register('post', PostViewSet)
router.register('post_like', PostLikeViewSet)
router.register('post_comment', PostCommentViewSet)

urlpatterns += router.urls
