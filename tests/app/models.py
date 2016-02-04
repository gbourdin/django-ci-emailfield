from django.db import models
from django_ciemailfield import CiEmailField


class User(models.Model):
    email = CiEmailField(unique=True)
