# Generated by Django 3.2.3 on 2022-05-12 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('rut_medico', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre_medico', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('rut_paciente', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre_paciente', models.CharField(max_length=30)),
                ('sexo_paciente', models.CharField(max_length=15)),
                ('edad_paciente', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FichaMedica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_medicamento', models.CharField(max_length=30)),
                ('observacion_paciente', models.CharField(max_length=100)),
                ('rut_medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultaMedica.medico')),
                ('rut_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultaMedica.paciente')),
            ],
        ),
    ]
