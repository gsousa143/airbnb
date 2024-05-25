from . models import *
from rest_framework import serializers


class RelacaoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Relacao
        fields = [
            'id',
            'inicio',
            'fim',
            'produto',
            'usuario',
            'nivel',
            'quantidade_crianca',
            'quantidade_adultos',
            'quantidade_bebes',
            'quantidade_pets'
                  ]
