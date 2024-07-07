from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Client(models.Model):
    name = models.CharField(max_length=35, verbose_name="name")
    last_name = models.CharField(max_length=35, verbose_name="last_name", **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='email')
    comment = models.TextField(verbose_name='comment', **NULLABLE)
    is_activ = models.BooleanField(default=False, verbose_name='activ')
    company = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.last_name} {self.name}"

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"


class Mailing(models.Model):
    name = models.CharField(max_length=50, verbose_name="tema")
    message = models.TextField(verbose_name="text")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created_at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated_at")
    clients = models.ManyToManyField(Client,  related_name="mailings", verbose_name="clients")
    is_active = models.BooleanField(default=True, verbose_name='active')
    is_deleted = models.BooleanField(default=False, verbose_name='deleted')
    send_count = models.PositiveIntegerField(default=0, verbose_name="send_count")
    error_count = models.PositiveIntegerField(default=0, verbose_name="error_count")
    last_send_at = models.DateTimeField(null=True, verbose_name="last_send_at")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.last_send_at})"

    class Meta:
        verbose_name = "рассылка"
        verbose_name_plural = "рассылки"


