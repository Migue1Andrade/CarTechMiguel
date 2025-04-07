from django.db import models

class Carro(models.Model):
    COMBUSTIVEL_CHOICES = [
        ('G', 'Gasolina'),
        ('E', 'Etanol'),
        ('F', 'Flex'),
        ('D', 'Diesel'),
        ('E+', 'Elétrico'),
        ('H', 'Híbrido'),
    ]

    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    ano_fabricacao = models.PositiveIntegerField()
    cor = models.CharField(max_length=30)
    placa = models.CharField(max_length=10, unique=True)
    tipo_combustivel = models.CharField(max_length=2, choices=COMBUSTIVEL_CHOICES)
    quilometragem = models.PositiveIntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    descricao = models.TextField(blank=True, default="Sem descrição")
    data_cadastro = models.DateTimeField(auto_now_add=True)
    img = models.URLField(default="https://via.placeholder.com/150")

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.placa})"
