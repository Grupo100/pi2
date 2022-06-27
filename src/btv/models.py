from django.db import models

# Create your models here.
class Doador(models.Model):
    nome = models.CharField(max_length=80)

    def __str__(self):
        return self.nome
    
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)


class Documento(models.Model):
    titulo = models.CharField(max_length=100)
    doador = models.ForeignKey(Doador, default=1, on_delete=models.SET_DEFAULT)
    pdf = models.FileField(upload_to="docs/")

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)