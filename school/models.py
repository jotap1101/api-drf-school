from django.db import models

# Create your models here.
class Course(models.Model):
    LEVELS_CHOICES = [
        ('B', 'Basic'),
        ('I', 'Intermediate'),
        ('A', 'Advanced')
    ]

    code = models.CharField(max_length=255, verbose_name='Código')
    name = models.CharField(max_length=255, verbose_name='Nome')
    level = models.CharField(max_length=255, choices=LEVELS_CHOICES, verbose_name='Nível')
    description = models.TextField(verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    rg = models.CharField(max_length=255, verbose_name='RG')
    cpf = models.CharField(max_length=255, verbose_name='CPF')
    birth_date = models.DateField(verbose_name='Data de Nascimento')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return self.name
    
class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('A', 'Active'),
        ('C', 'Canceled'),
        ('P', 'Pending')
    ]

    PERIOD_CHOICES = [
        ('M', 'Morning'),
        ('A', 'Afternoon'),
        ('N', 'Night')
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Aluno')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Curso')
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='P', verbose_name='Status')
    period = models.CharField(max_length=255, choices=PERIOD_CHOICES, verbose_name='Período')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Matrícula'
        verbose_name_plural = 'Matrículas'

    def __str__(self):
        return f'{self.student} - {self.course}'