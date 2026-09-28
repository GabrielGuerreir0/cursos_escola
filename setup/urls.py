from django.contrib import admin
from django.urls import path, include
from escola.views import EstudantesViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculaEstudante, ListaMatriculaCurso
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('estudantes',EstudantesViewSet, basename='Estudantes')
routers.register('cursos', CursoViewSet, basename='Cursos')
routers.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(routers.urls)),
    path('estudantes/<int:pk>/matriculas/', ListaMatriculaEstudante.as_view()),
    path('curso/<int:pk>/matriculas/', ListaMatriculaCurso.as_view())
]
