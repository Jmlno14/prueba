from django.db import models

class Country(models.Model):
    nombreCountry = models.CharField('nombreCountry', max_length=52, null=False)
    id_country = models.CharField('nombreCountry', max_length=3, unique=True, null=False)
    continent_Country = models.IntegerField('continentCountry', null=False)
    region_Country = models.CharField('regionCountry', max_length=20, null=False)
    surface_Country = models.DecimalField('countryArea', max_digits=10, decimal_places=2, null=False)
    indep_year_country = models.SmallIntegerField('idepCountry', null=True)
    population = models.IntegerField('populationCountry', null=False)
    life_expectancy = models.DecimalField('lifeExpectancy', max_digits=5, decimal_places=2, null=True)
    GNP = models.DecimalField('GNPCountry', max_digits=10, decimal_places=2, null=True)
    GNPold = models.DecimalField('GNPold', max_digits=10, decimal_places=2, null=True)
    local_name = models.CharField('countryLocalname', max_length=45, null=False)
    goverment = models.CharField('countryGoverment', max_length=45, null=False)
    state_head = models.CharField('countryLeader', max_length=60, null=True)
    capital_country = models.IntegerField('capitalId', null=True)
    code2 = models.CharField('countryCode2', max_length=2, null=False)

    siglaCountry = models.CharField('siglaCountry', max_length=2, unique=True)
    activoCountry = models.BooleanField('active', default=False)
    search_fields = ('nombreCountry', 'siglaCountry',)
    list_filter = ('nombreCountry',)

    class Meta:
        verbose_name = 'Nombre Country'
        verbose_name_plural = 'Nombres Countrys'
        ordering = ['nombreCountry']
        unique_together = ('nombreCountry', 'siglaCountry')

    def __str__(self):
        return self.nombreCountry + ' - ' + self.siglaCountry + str(self.id)
