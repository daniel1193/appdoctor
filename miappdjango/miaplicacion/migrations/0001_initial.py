# Generated by Django 3.0.7 on 2020-10-15 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormulasPacientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.IntegerField()),
                ('fecha', models.DateField()),
                ('medicamento', models.CharField(max_length=20)),
                ('cantidad', models.CharField(max_length=30)),
                ('dosis', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='HistoriaPaciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.IntegerField(max_length=10)),
                ('correo', models.EmailField(max_length=254)),
                ('patologia', models.CharField(max_length=50)),
                ('remisiones', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('especialidad', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='MedicosDisponibles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('especialidad', models.CharField(max_length=45)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
    ]
