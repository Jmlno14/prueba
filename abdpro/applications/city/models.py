from django.db import models
from django.db import models

class City(models.Model):
    nombre_city = models.CharField('nombreCity', max_length=35)
    id_country = models.CharField('nombreCountry', max_length=3)
    id_city = models.CharField('idCity', max_length=11, primary_key=True)
    population_city = models.IntegerField('population', max_length=11)
    district_city = models.CharField('district', max_length=20)
    sigla_city = models.CharField('siglaCity', max_length=2, unique=True)
    activo_city = models.BooleanField('active', default=False)

    class Meta:
        verbose_name = 'Nombre City'
        verbose_name_plural = 'Nombres Citys'
        ordering = ['nombre_city']
        unique_together = ('nombre_city', 'sigla_city')

    def __str__(self):
        return f"{self.nombre_city} - {self.sigla_city} {str(self.id_city)}"

