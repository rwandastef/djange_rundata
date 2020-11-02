from rest_framework import serializers
from uitslagen.models import Uitslag

class UitslagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uitslag
        fields = ('label', 'time', 'gender', 'dayNumber', 'temperature', 'regioCode')
