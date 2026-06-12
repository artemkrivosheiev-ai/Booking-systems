from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('rooms/', views.room_list, name='room_list'),

    path('reviews/', views.review_list, name='review_list'),
    path('reviews/<int:id>/', views.review_detail, name='review_detail'),

    path('booking/', views.create_booking, name='create_booking'),
]
