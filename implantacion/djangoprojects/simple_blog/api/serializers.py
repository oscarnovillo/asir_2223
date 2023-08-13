from rest_framework import serializers
from api.models import Coche,Accidente


        
class AccidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accidente
        fields = '__all__'

class CocheSerializer(serializers.ModelSerializer):
    accidentes = AccidenteSerializer(many=True)
    
    class Meta:
        model = Coche
        fields = '__all__'
