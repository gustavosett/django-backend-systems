from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


def index(request):
    teste = {
        'teste': request
    }
    return render(request, 'index.html', teste)


class CursoAPIView(APIView):
    """
    API DE CURSOS
    """
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)


class AvaliacaoAPIView(APIView):
    """
    API de Avaliações
    """
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)