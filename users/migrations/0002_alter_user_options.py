# Generated by Django 4.2.2 on 2024-07-22 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('deactivate_user', 'Can deactivate user'), ('view_all_users', 'Can view all users')], 'verbose_name': 'пользователь', 'verbose_name_plural': 'пользователи'},
        ),
    ]
