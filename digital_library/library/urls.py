from django.urls import path, include
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/new/', views.book_create, name='book_create'),
    path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),
]