# Generated by Django 4.1 on 2022-09-06 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Empleados", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="direccionempleado",
            name="ciudad",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="direccionempleado",
            name="direccion",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="direccionempleado",
            name="pais",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="direccionempleado",
            name="provincia",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="empleado",
            name="employee_dni",
            field=models.CharField(max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name="empleado",
            name="employee_hire_date",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="empleado",
            name="employee_name",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="empleado",
            name="employee_surname",
            field=models.CharField(max_length=30),
        ),
    ]
