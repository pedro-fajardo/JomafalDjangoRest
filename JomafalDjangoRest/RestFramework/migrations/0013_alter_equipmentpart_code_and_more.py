# Generated by Django 5.1.2 on 2024-11-09 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestFramework', '0012_remove_equipment_parts_equipmentpart_equipment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentpart',
            name='code',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipmentpart',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipmentpart',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipmentpart',
            name='value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
