from django.db import models


class Voto(models.Model):
    class Genero(models.TextChoices):
        MASCULINO = 'M', 'Masculino'
        FEMININO = 'F', 'Feminino'
        OUTRO = 'O', 'Outro/Prefiro não dizer'
    genero = models.CharField(max_length=1, choices=Genero.choices, verbose_name='gênero')

    idade = models.PositiveSmallIntegerField()

    class Dispositivo(models.TextChoices):
        DESKTOP = 'Desktop'
        NOTEBOOK = 'Notebook'
        TABLET = 'Tablet'
        SMARTPHONE = 'Smartphone'
        OUTRO = 'Outro'
    dispositivo = models.CharField(max_length=10, choices=Dispositivo.choices)

    class Opiniao(models.IntegerChoices):
        MUITO_FAVORAVEL = 1, 'Muito Favorável'
        FAVORAVEL = 2, 'Favorável'
        NEUTRA = 3, 'Neutra'
        DESFAVORAVEL = 4, 'Desfavorável'
        MUITO_DESFAVORAVEL = 5, 'Muito Desfavorável'
    opiniao = models.PositiveSmallIntegerField(choices=Opiniao.choices)

    class Cor(models.TextChoices):
        RED = 'Red'
        GREEN = 'Green'
        BLUE = 'Blue'
        CYAN = 'Cyan'
        MAGENTA = 'Magenta'
        YELLOW = 'Yellow'
        BLACK = 'Black'
        WHITE = 'White'
    cor = models.CharField(max_length=10, choices=Cor.choices)

    def __str__(self) -> str:
        return f'#{self.pk}'

    @property
    def as_payload(self):
        return {f.name: getattr(self, f.name) for f in Voto._meta.fields}  # if f.name != 'id'
