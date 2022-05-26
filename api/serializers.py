from pyexpat import model
from rest_framework import serializers
from .models import Prognosis

class PrognosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prognosis
        fields = '__all__'