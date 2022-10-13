from django.urls import path
from . import views








urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<str:slug>/detail/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path("register/", views.register, name="register"),
    path('post/<str:slug>/edit/', views.post_edit, name='post_edit'),
    path("login/", views.login, name="login"),
    path("logout/", views.logout_user, name='logout_page'),
    path('category/<str:slug>', views.category_list, name = 'category_list'),
    path('tags/<str:slug>', views.tags_list, name = 'tags_list'),
    path('profile', views.profile_page, name = 'profile'),
    path('edit-profile/', views.edit_profile, name = 'edit-profile'),
    
    
]
