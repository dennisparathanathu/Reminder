from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('reg/', views.register, name='register'),
    path('dash/', views.dashbord, name='dashbord'),
    path('logout/', views.logout, name='logout'),
    path('addreminder/', views.add_reminder, name='add_reminder'),
    path('edit/<int:pk>', views.edit_reminder, name='edit_reminder'), path('delete_remin/<int:pk>', views.delete_reminder, name='delete_reminder'),
]


