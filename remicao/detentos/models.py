

# Create your models here.
from django.db import models

class Detento(models.Model):
    nome = models.CharField(max_length=200)
    processo = models.CharField(max_length=50)
    pena_total_dias = models.IntegerField()
    data_inicio = models.DateField()

    def __str__(self):
        return self.nome


class Atividade(models.Model):
    TIPOS = [
        ('TRABALHO', 'Trabalho'),
        ('ESTUDO', 'Estudo'),
        ('LEITURA', 'Leitura'),
    ]
    detento = models.ForeignKey(Detento, on_delete=models.CASCADE, related_name="atividades")
    tipo = models.CharField(max_length=10, choices=TIPOS)
    quantidade = models.IntegerField(help_text="Dias trabalhados, horas de estudo ou livros lidos")
    data_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.detento.nome}"
