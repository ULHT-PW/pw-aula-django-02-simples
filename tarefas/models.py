from django.db import models

# Create your models here.
class Tarefa(models.Model):

    titulo = models.CharField(max_length=50)
    prioridade = models.IntegerField(default=1)
    concluida = models.BooleanField(default=False)
    criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo}"
