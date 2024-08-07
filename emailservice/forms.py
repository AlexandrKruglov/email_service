from django.forms import ModelForm
from django.shortcuts import get_object_or_404

from emailservice.models import Mailing, Client
from users.models import User


class MailingForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        user = self.request.user
        super().__init__(*args, **kwargs)
        self.fields['clients'].queryset = []
        # self.fields['clients'].queryset = Client.objects.filter(owner=self.instance.owner)

    class Meta:
        model = Mailing
        fields = ('name', 'message', 'clients', 'period_mail', 'start_mail', 'stop_mail', 'next_send_time')


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
