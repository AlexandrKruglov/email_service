# Generated by Django 4.2.2 on 2024-07-21 16:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emailservice', '0008_remove_client_is_activ_alter_mailing_stop_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='stop_mail',
            field=models.DateField(default=datetime.datetime(2024, 7, 22, 16, 20, 10, 585293, tzinfo=datetime.timezone.utc), verbose_name='Конец рассылки'),
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время попытки отправки')),
                ('status', models.CharField(choices=[('Успешно', 'Успешно'), ('Неуспешно', 'Неуспешно')], max_length=50, verbose_name='Cтатус рассылки')),
                ('server_response', models.CharField(blank=True, max_length=150, null=True, verbose_name='Ответ сервера почтового сервиса')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emailservice.mailing', verbose_name='Рассылка')),
            ],
            options={
                'verbose_name': 'Попытка рассылки',
                'verbose_name_plural': 'Попытки рассылки',
            },
        ),
    ]
