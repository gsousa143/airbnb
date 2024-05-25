from django.db import models

class Tag(models.Model):
    nome = models.CharField(max_length =50)
    def __str__(self):
        return self.nome
    
class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome
    
class Nivel(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome
    
class Tipo(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(null=True)
    valor = models.IntegerField()
    tipo = models.ForeignKey(Tipo,on_delete=models.SET_NULL,null=True)
    limite_adultos = models.IntegerField()
    limite_criancas = models.IntegerField()
    limite_bebes = models.IntegerField()
    limite_pets = models.IntegerField()

    def __str__(self):
        return self.nome

class Auxiliar(models.Model):
    produto = models.ForeignKey(Produto,on_delete=models.SET_NULL,null=True)
    tag = models.ForeignKey(Tag,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.produto.nome+"_"+self.tag.nome


class Relacao(models.Model):
    inicio = models.DateField()
    fim = models.DateField()
    produto = models.ForeignKey(Produto,on_delete=models.SET_NULL,null=True)
    usuario = models.ForeignKey(Usuario,on_delete=models.SET_NULL,null=True)
    nivel = models.ForeignKey(Nivel,on_delete=models.SET_NULL,null=True)
    quantidade_crianca = models.IntegerField()
    quantidade_adultos = models.IntegerField()
    quantidade_bebes = models.IntegerField()
    quantidade_pets = models.IntegerField()

    def __str__(self):
        return self.usuario.nome+"_"+self.produto.nome