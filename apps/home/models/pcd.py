from django.db import models
from apps.home.models import Pessoa



class Pcd(Pessoa):
    id_estrangeiro = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = "PcD"
