# Generated by Django 4.2.2 on 2023-06-21 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("proposal", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="proposal",
            name="status",
            field=models.CharField(
                choices=[("Negada", "Negada"), ("Aprovada", "Aprovada")],
                max_length=8,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="address",
            name="proposal",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="address",
                to="proposal.proposal",
            ),
        ),
    ]
