from django.urls import path, include
from blog.api import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('user',views.UserViewSet, basename = 'user')
router.register(r'posts',views.PostViewSet, basename = 'post')
router.register(r'post_detail',views.PostDetail, basename = 'post_detail')
router.register(r'comments',views.CommentViewSet, basename = 'comment')
router.register(r'post_category', views.CategoryViewSet, basename = 'category')
router.register(r'post_tags', views.TagsViewSet, basename = 'tags')


urlpatterns = [
    path("", include(router.urls)),
    # path("api_post/", include(router.urls)),
    
    # path("api_comment/", include(router.urls))
 ]