from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.custom_login_view, name='accounts-login' ),
    path('signup/', views.signup_view, name='accounts-signup'),
    path('logout/', views.CustomLogoutView.as_view(), name='accounts-logout'),
    path('', views.index_view, name='accounts-index')

]
