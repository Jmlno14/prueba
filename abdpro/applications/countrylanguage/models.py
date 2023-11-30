from django.db import models

class Countrylanguage(models.Model):
    nombreCountrylanguage = models.CharField('nombreCountrylanguage', max_length=35)
    id_country = models.CharField('nombreCountry', max_length=3, unique=True, null=False)
    Countrylanguage = models.CharField('Countrylanguage', max_length=30, null=False)
    isOfficial = models.BooleanField('officialanguage', null=False)
    percentage = models.DecimalField('languagePercentaje', max_digits=4, decimal_places=1, null=False)  # Corregidos max_digits y decimal_places
    siglaCountrylanguage = models.CharField('siglaCountrylanguage', max_length=2, unique=True)
    activoCountrylanguage = models.BooleanField('active', default=False)
    search_fields = ('nombreCountrylanguage', 'siglaCountrylanguage',)
    list_filter = ('nombreCountrylanguage',)

    class Meta:
        verbose_name = 'Nombre Countrylanguage'
        verbose_name_plural = 'Nombres Countrylanguages'
        ordering = ['nombreCountrylanguage']
        unique_together = ('nombreCountrylanguage', 'siglaCountrylanguage')

    def __str__(self):
        return self.nombreCountrylanguage + ' - ' + self.siglaCountrylanguage + str(self.id)
