from django.urls import path
from . import views

urlpatterns = [
    path('todolistapp', views.index, name='index'),
    path('edit/<int:edit_id>', views.edit, name='edit'),
    path('delete/<int:delete_id>', views.delete, name='delete'),
    path('register', views.register, name='register'),
    path('login', views.loginuser, name='loginuser'),
    path('logout', views.logoutuser, name='logoutuser'),
    path('', views.home, name='home'),
    ]