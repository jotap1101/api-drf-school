# Generated by Django 5.0.4 on 2024-05-05 20:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_course_options_alter_student_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('A', 'Active'), ('C', 'Canceled'), ('P', 'Pending')], default='P', max_length=255, verbose_name='Status')),
                ('period', models.CharField(choices=[('M', 'Morning'), ('A', 'Afternoon'), ('N', 'Night')], max_length=255, verbose_name='Período')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.course', verbose_name='Curso')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.student', verbose_name='Aluno')),
            ],
            options={
                'verbose_name': 'Matrícula',
                'verbose_name_plural': 'Matrículas',
            },
        ),
    ]
