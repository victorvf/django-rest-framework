from django.contrib.auth.models import User
from django.db import models

class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    nota = models.DecimalField(max_digits=2,decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username
