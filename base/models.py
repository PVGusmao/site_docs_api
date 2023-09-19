from django.db import models

class Pacients(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    cpf = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)