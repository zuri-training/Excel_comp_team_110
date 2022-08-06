from re import template
from django.urls import path
from . import views
from .views import profile_user
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('register_user', views.register_user, name="register"),
    path('profile_user', views.profile_user, name="profile"),
    path('password', auth_views.PasswordChangeView.as_view(template_name = 'registration/change-password.html')),
    # path('change_password', views.change_password, name="change_password"),
    # path('password_done', views.password_done, name="password_done")
]