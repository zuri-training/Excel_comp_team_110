from django.urls import path
from . import views
from .views import profile_user

urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('register_user', views.register_user, name="register"),
    path('profile_user', profile_user, name="profile"),
    path('change_password', views.change_password, name="change password"),
]