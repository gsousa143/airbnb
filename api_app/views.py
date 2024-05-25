from django.shortcuts import render

from rest_framework.decorators import api_view

from .models import *

from .serializers import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(["GET","POST"])
def relacao(request):
    if request.method == "GET":
        relacoes = Relacao.objects.all()
        serializer = RelacaoSerializer(relacoes,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == "POST":
        serializer = RelacaoSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    


@api_view(["GET","PUT","DELETE"])
def relacao_id(request,id):
    try:
        relacao = Relacao.objects.get(id=id)
    except Relacao.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = RelacaoSerializer(relacao)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = RelacaoSerializer(instance=relacao,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        relacao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


