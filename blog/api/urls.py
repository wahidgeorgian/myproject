from django.urls import path, include
from blog.api import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('crud',views.UserViewSet, basename = 'user')
router.register(r'posts',views.PostViewSet, basename = 'post')
router.register(r'comments',views.CommentViewSet, basename = 'comment')


urlpatterns = [
    path("", include(router.urls)),
    # path("api_post/", include(router.urls)),
    
    # path("api_comment/", include(router.urls))
 ]