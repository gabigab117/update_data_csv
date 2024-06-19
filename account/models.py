from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class UserData(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, verbose_name="Utilisateur")
    index = models.IntegerField(blank=True, null=True)
