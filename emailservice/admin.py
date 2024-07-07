from django.contrib import admin

from emailservice.models import Mailing, Client


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'owner', 'is_active')
    list_filter = ('owner',)
    search_fields = ('name', 'owner')



@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'last_name', 'company')
    list_filter = ('company',)
    search_fields = ('email', 'company')
