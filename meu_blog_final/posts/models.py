from django.db import models
from django.contrib.auth.models import User


LINGUAGENS = [
    ('PY', 'Python'),
    ('JS', 'JavaScript'),
    ('JAVA', 'Java'),
    ('CS', 'C#'),
]

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    linguagem = models.CharField(max_length=4, choices=LINGUAGENS, default='PY') # Novo campo
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo