# Generated by Django 4.1 on 2022-09-07 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Sucursales", "0008_alter_sucursal_branch_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sucursal",
            name="branch_name",
            field=models.CharField(max_length=30),
        ),
    ]
