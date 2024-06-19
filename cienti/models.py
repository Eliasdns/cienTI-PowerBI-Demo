from django.db import models
from django.db.models import Q, Count, Avg


class Voto(models.Model):
    class Genero(models.TextChoices):
        MASCULINO = 'M', 'Masculino'
        FEMININO = 'F', 'Feminino'
        OUTRO = 'O', 'Outro/Prefiro não dizer'

    class Dispositivo(models.TextChoices):
        DESKTOP = 'Desktop'
        NOTEBOOK = 'Notebook'
        TABLET = 'Tablet'
        SMARTPHONE = 'Smartphone'
        OUTRO = 'Outro'

    class Opiniao(models.IntegerChoices):
        MUITO_FAVORAVEL = 1, 'Muito Favorável'
        FAVORAVEL = 2, 'Favorável'
        NEUTRA = 3, 'Neutra'
        DESFAVORAVEL = 4, 'Desfavorável'
        MUITO_DESFAVORAVEL = 5, 'Muito Desfavorável'

    class Cor(models.TextChoices):
        RED = 'Red'
        GREEN = 'Green'
        BLUE = 'Blue'
        CYAN = 'Cyan'
        MAGENTA = 'Magenta'
        YELLOW = 'Yellow'
        BLACK = 'Black'
        WHITE = 'White'

    class VotoManager(models.Manager):
        def aggs_as_payload(self):
            aggregates = self.aggregate(
                total_votos=Count('id'),
                total_genero_masculino=Count('id', filter=Q(genero=Voto.Genero.MASCULINO)),
                total_genero_feminino=Count('id', filter=Q(genero=Voto.Genero.FEMININO)),
                media_idade=Avg('idade'),
                media_opiniao=Avg('opiniao'),
            )

            preferred_dispositivo = self.values('dispositivo').annotate(count=Count('dispositivo')).order_by('-count').first()
            preferred_cor = self.values('cor').annotate(count=Count('cor')).order_by('-count').first()

            aggregates['preferred_dispositivo'] = preferred_dispositivo['dispositivo'] if preferred_dispositivo else None
            aggregates['preferred_cor'] = preferred_cor['cor'] if preferred_cor else None

            return aggregates
    objects = VotoManager()

    genero = models.CharField(max_length=1, choices=Genero.choices, verbose_name='gênero')
    idade = models.PositiveSmallIntegerField()
    dispositivo = models.CharField(max_length=10, choices=Dispositivo.choices)
    opiniao = models.PositiveSmallIntegerField(choices=Opiniao.choices)
    cor = models.CharField(max_length=10, choices=Cor.choices)

    def __str__(self):
        return f'#{self.pk}, {self.genero}, {self.idade}y, {self.dispositivo}, IA: {self.opiniao}, {self.cor}'

    @property
    def obj_as_payload(self):
        return {f.name: getattr(self, f.name) for f in Voto._meta.fields}  # if f.name != 'id'
