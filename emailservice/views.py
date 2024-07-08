from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from emailservice.models import Mailing


class EmailservicePageVeiw(TemplateView):
    template_name = 'emailservice/start.html'


class EmailserviceListView(ListView):
    model = Mailing
    template_name = 'emailservice/lk.html'
