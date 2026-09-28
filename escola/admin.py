from django.contrib import admin
from escola.models import Estudante,Curso,Matricula

class Estudantes(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'cpf','date_birth', 'phone')
    list_display_links = ('id', 'name',)
    list_per_page = 20
    search_fields = ('name',)

admin.site.register(Estudante, Estudantes)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'description')
    list_display_links = ('id', 'codigo',)
    search_fields = ('codigo',)

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'period',)
    list_display_links = ('id',)

admin.site.register = ('Matricula', 'Matriculas')