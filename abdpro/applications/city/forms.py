# ------------------------------------------------------------------
# DJANGO
# ------------------------------------------------------------------

from django import forms

# ------------------------------------------------------------------
# MODELO
# ------------------------------------------------------------------

from .models import City

# ------------------------------------------------------------------
# FORMULARIO
# ------------------------------------------------------------------
class NuevoCityForm(forms.ModelForm):
    """Form definition for City."""
    class Meta:
        """Meta definition for Cityform."""
        # Modelo al que se aplica el formulario
        model = City
        # Campos usados en el formulario
        fields = (
                'nombre_city',
                'population_city',
                'district_city',
                'sigla_city',
                'activo_city'
        )
        # Labels de los campos del formulario
        labels = {
            'nombre_City': 'Nombre City',
            'sigla_City': 'Sigla City',
            'activo_City': 'Activo',
            'population_City': 'population',
            'district_City': 'district City'
        }
                # Espacio para agregar características a los campos
        widgets = {
            'activoCity': forms.CheckboxInput(
                attrs={'class': 'ContainerCityFormSelect'}
            ),
            'nombreCity': forms.TextInput(
                attrs={
                    'class': 'ContainerCityFormName',
                    'placeholder': 'Nombre City'
                }
            ),
            'siglaCity': forms.TextInput(
                attrs={
                    'class': 'ContainerCityFormName',
                    'placeholder': 'Sigla City'
                }
            ),
        }