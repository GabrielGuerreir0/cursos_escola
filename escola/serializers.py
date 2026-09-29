from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'name', 'email', 'cpf', 'date_birth', 'phone']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='curso.description')
    period = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['course','period']
    def get_period(self,obg):
        return obg.get_period_display()

class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source = 'estudante.name') 
    class Meta:
        model = Matricula
        fields = ['student_name']
