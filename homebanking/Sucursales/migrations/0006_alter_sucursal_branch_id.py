# Generated by Django 4.1 on 2022-09-07 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Sucursales", "0005_remove_sucursal_branch_address_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sucursal",
            name="branch_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]