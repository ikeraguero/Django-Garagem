from django.db import models

class Carro(models.Model):
    modelo=models.CharField(max_length=50)
    marca=models.ForeignKey(
        Marca, on_delete=models.PROTECT, related_name="carros")
    categoria=models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="carros"
    )
    ano = models.IntegerField(null=True, blank=True)
    cor = models.CharField(max_length=50, null=True, blank=True)
    preco = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.cor} ({self.ano})"