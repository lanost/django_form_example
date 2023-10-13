# user_management/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('student/', views.student_view, name='student'),
    path('staff/', views.staff_view, name='staff'),
    path('custom_admin/', views.admin_view, name='admin'),
    path('editor/', views.editor_view, name='editor'),
    path('logout/', views.custom_logout, name='logout'),

    # Define URLs for other roles
]
