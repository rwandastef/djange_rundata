from rest_framework import serializers
from uitslagen.models import Uitslag, AnalysedUitslagen


class UitslagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uitslag
        fields = ('label', 'time', 'gender', 'dayNumber', 'temperature', 'regioCode')

class AnalysedUitslagenSerializer(serializers.Serializer):
    mean_runtime = serializers.FloatField(default=0)