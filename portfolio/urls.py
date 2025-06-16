from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='portfolio-home'),
    path('my-profile/', views.my_profile, name='portfolio-my-profile'),
    path('<int: profile_id>/detail/', views.detail, name='portfolio-detail'),
]