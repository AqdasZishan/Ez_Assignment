from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Login page
    path('boss/', views.boss_dashboard, name='boss_dashboard'),  # Custom Admin (Boss) portal
    path('user/', views.user_dashboard, name='user_dashboard'),  # User portal
]
