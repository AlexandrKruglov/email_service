from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateView, activate  # ,  UserPasswordResetView, activate

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('activate/<str:token>/', activate, name='activate'),
    # path('password-reset/', UserPasswordResetView.as_view(template_name="users/password_reset_form.html"),
    #      name='password-reset'),
]
