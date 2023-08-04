from django.contrib import admin
from django.urls import path,include
from .views import posts,postsdetails,like,unlike,comment,users,follow
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('posts',posts),
    path("posts/<int:pk>",postsdetails),
    path('like/<int:pk>',like),
    path('unlike/<int:pk>',unlike),
    path('all_posts',posts),
    path('comment/<int:pk>',comment),
    path('user/<int:user_id>',users),
    path('follow/<int:user_id>',follow),
    path('authenticate/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('authenticate/refresh/',TokenRefreshView.as_view(),name = "token_refresh")
]