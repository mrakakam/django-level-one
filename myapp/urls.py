from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path ('post/new/', views.post_create, name='post_create'),  #added int cause we gave pk as integer in views.py
    path('post/<int:pk>/', views.post_details, name='post_detail'),  #added int cause we gave pk as integer in views.py
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),  #added int cause we gave pk as integer in views.py
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'), #added int cause we gave pk as integer in views.py
]
