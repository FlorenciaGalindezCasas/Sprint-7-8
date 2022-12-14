# Generated by Django 4.1 on 2022-09-07 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Sucursales", "0004_remove_sucursal_loan_id"),
        ("Clientes", "0008_remove_cliente_branch_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="cliente",
            name="branch_id",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="Sucursales.sucursal",
            ),
            preserve_default=False,
        ),
    ]
