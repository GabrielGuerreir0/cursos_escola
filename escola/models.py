from django.db import models
from django.core.validators import MinLengthValidator

class Estudante(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(blank = False, max_length = 30)
    cpf = models.CharField(max_length = 11, unique = True)
    date_birth = models.DateField()
    phone = models.CharField(max_length = 14)

    def __str__(self):
        return self.name

class Curso(models.Model):
    LEVEL = (
        ('B','Basico'),
        ('I','Intermediario'),
        ('A','Avancado'),
    )
    codigo = models.CharField(max_length = 10, unique = True, validators = [MinLengthValidator(3)])
    description = models.CharField(max_length = 100, blank=False)
    level = models.CharField(max_length = 1, choices = LEVEL, blank = False, null = False, default= 'B')

    def __str__(self):
        return self.codigo

class Matricula(models.Model):
    PERIOD = (
        ('M','Manha'),
        ('T','Tarde'),
        ('N','Noite'),
    )
    student = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    course = models.ForeignKey(Curso, on_delete=models.CASCADE)
    period = models.CharField(max_length = 1, choices=PERIOD, blank = False, null = False, default='M')
