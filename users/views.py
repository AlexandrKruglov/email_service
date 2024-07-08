import secrets

from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserRecoveryForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class UserPasswordResetView(PasswordResetView):
    form_class = UserRecoveryForm
    template_name = 'users/password_reset_form.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        if self.request.method == 'POST':
            user_email = self.request.POST.get('email')
            user = User.objects.filter(email=user_email).first()
            if user:
                new_password = secrets.token_hex(10)
                user.set_password(new_password)
                user.save()
                send_mail(
                    subject="Восстановление пароля",
                    message=f"Здравствуйте. Ваш пароль  изменен:\n"
                            f"Новый пароль: {new_password}\n"
                            f"Вы можете изменить его в своем профиле",
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[user.email]
                )

            return HttpResponseRedirect(reverse('users:login'))
