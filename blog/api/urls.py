from django.urls import path, include
from blog.api import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('crud',views.UserViewSet, basename = 'user')
router.register('crud',views.PostViewSet, basename = 'post')
# router.register('crud',views.CommentViewSet, basename = 'comment')


urlpatterns = [
    path("", include(router.urls)),
    path("api_post/", include(router.urls)),
    path("api_comment/", include(router.urls))
]