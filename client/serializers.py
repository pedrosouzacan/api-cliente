from rest_framework import serializers
from client.models import Client
from client.validators import *

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def validate_cpf(self,cpf):
        if len(cpf)!=11:
          raise serializers.ValidationError('CPF inválido!')
        return cpf

    def validate_rg(self,rg):
        if len(rg)!=9:
            raise serializers.ValidationError('RG deve ter 9 dígitos!')
        return rg
    
    def validate(self,data):
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'Celular':'Número de celular deve seguir este modelo: 19 99999-9999'})
        return data
