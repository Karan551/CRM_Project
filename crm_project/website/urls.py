from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('record/<int:user_id>/', views.user_record, name='user_record'),
    path('delete/<int:user_id>/', views.delete_record, name='delete_record'),
    path("add_record/", views.add_record, name="add_record"),
    path("update_record/<int:user_id>/", views.update_record, name="update_record"),
]
