from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
from escola.validators import cpf_invalido, name_invalido, phone_invalido

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'name', 'email', 'cpf', 'date_birth', 'phone']

    def validate(self, data):

        if cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"O cpf informado tem formato invalido!"})
        if name_invalido(data['name']):
            raise serializers.ValidationError({'name':"O nome so pode ter letras"})
        if phone_invalido(data['phone']):
            raise serializers.ValidationError({'phone':"O telefone deve ter o modelo XX XXXXX-XXXX"})

        return data

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


class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'name', 'email', 'phone']