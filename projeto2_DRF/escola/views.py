from rest_framework import viewsets
from escola.models import Aluno, Curso
from escola.serializer import AlunoSerializer, CursoSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibir todos os alunos"""

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursoViewSet(viewsets.ModelViewSet):
    """Exibir todos os cursos"""

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
