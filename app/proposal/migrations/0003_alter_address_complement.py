# Generated by Django 4.2.2 on 2023-06-23 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposal', '0002_proposal_status_alter_address_proposal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='complement',
            field=models.CharField(max_length=100, null=True),
        ),
    ]