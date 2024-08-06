from django.forms import ModelForm
from django.shortcuts import get_object_or_404

from emailservice.models import Mailing, Client
from users.models import User


class MailingForm(ModelForm):
    class Meta:
        model = Mailing
        fields = ('name', 'message', 'clients', 'period_mail', 'start_mail', 'stop_mail', 'next_send_time')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     user =
    #
    #     self.fields['clients'].queryset = Client.user.filter(user=user)


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
