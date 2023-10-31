from rest_framework import serializers
from clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate_cpf(self, cpf):
        if (len(cpf) != 11):
            raise serializers.ValidationError("O CPF deve ter 11 digitos")
        return cpf
    
    def validate_name(self, nome):
        if not (nome.isalph()):
            raise serializers.ValidationError("O NOME deve conter apenas digitos")
        return nome


    