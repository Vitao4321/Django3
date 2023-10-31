from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"O CPF deve conter 11 digitos"})
        return data
    
    def validate_name(self, nome):
        if not nome.isalph():
            raise serializers.ValidationError("O NOME deve conter apenas letras")
        return nome

    def validate_rg(self, rg):
        if (len(rg) != 9):
            raise serializers.ValidationError("O RG deve ter 9 digitos")
        return rg
    
    def validate_phone(self, celular):
        if len(celular) < 11:
            raise serializers.ValidationError("O celular deve ter 11 digitos")
        return celular


    