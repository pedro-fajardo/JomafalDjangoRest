# Generated by Django 5.1.1 on 2024-11-04 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestFramework', '0008_equipmentpart_equipment_partsiva'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='parts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='RestFramework.equipmentpart'),
        ),
    ]
