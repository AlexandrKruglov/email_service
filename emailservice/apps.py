import os

from django.apps import AppConfig


class EmailserviceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'emailservice'

    def ready(self):
        from emailservice.services import start
        start()
