# Generated by Django 4.1 on 2022-09-06 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Sucursales", "0002_alter_sucursal_branch_name"),
        ("Prestamos", "0004_alter_prestamo_loan_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="prestamo",
            name="branch_name",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="Sucursales.sucursal",
            ),
            preserve_default=False,
        ),
    ]
