from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.analytics, name='analytics'),
    path('manage-posts/', views.manage_posts, name='manage_posts'),
    path('create-post/', views.create_post, name='create_post'),
    path('edit-post/<int:pk>/', views.edit_post, name='edit_post'),
    path('delete-post/<int:pk>/', views.delete_post, name='delete_post'),
]
