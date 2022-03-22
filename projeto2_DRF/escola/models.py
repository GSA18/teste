from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome


class Curso(models.Model):
    NIVEL = (("B", "Basico"), ("I", "Intermediario"), ("A", "Avançado"))
    cod = models.CharField(max_length=10)
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    nivel = models.CharField(
        max_length=1, choices=NIVEL, blank=False, null=False, default="B"
    )

    def __str__(self) -> str:
        return f'Cod: {self.cod}// Nome curso{self.nome}'