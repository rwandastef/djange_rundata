from rest_framework import serializers
from uitslagen.models import Uitslag
from weer.models import Weer, WeerAnalyse


class WeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weer
        fields = ('YYYYMMDD')

class WeerAnalyseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeerAnalyse
        fields = ('slope', 'intercept', 'rvalue', 'pvalue')