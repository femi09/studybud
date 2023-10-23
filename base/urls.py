from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('rooms/<str:pk>/', views.room, name="rooms"),
    path('create/', views.createRoom, name="create-room"),
    path('update/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete/<str:pk>/', views.deleteRoom, name="delete-room")
]
