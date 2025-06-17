from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.custom_login_view, name='accounts-login' ),
    path('signup/', views.signup_view, name='accounts-signup')
]
