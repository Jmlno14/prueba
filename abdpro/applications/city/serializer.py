from rest_framework import serializers, pagination

from .models import(
    City
)

class CitysSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('__all__')
