from django.urls import path

from emailservice.apps import EmailserviceConfig
from emailservice.views import EmailservicePageVeiw, EmailserviceListView

app_name = EmailserviceConfig.name

urlpatterns = [
    path('', EmailservicePageVeiw.as_view(), name='home'),
    path('lk', EmailserviceListView.as_view(), name='lk')
]
