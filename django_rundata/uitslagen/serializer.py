from rest_framework import serializers
from uitslagen.models import Uitslag, AnalysedUitslagen


class UitslagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uitslag
        fields = ('label', 'time', 'gender', 'dayNumber', 'temperature', 'regioCode')

class AnalysedUitslagenSerializer(serializers.Serializer):
    mean_runtime = serializers.FloatField(default=0)
    slope = serializers.FloatField(default=0)
    intercept = serializers.FloatField(default=0)
    pvalue = serializers.FloatField(default=0)
    rvalue = serializers.FloatField(default=0)
    mean_runtime_men = serializers.FloatField(default=0)
    mean_runtime_women = serializers.FloatField(default=0)