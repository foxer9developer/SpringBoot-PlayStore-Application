# Generated by Django 3.1.1 on 2020-10-19 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IIT_OpenOCR', '0014_auto_20201019_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sets',
            name='status',
            field=models.CharField(choices=[('Set OCRed', 'Set OCRed'), ('Corrector', 'Corrector'), ('Verifier', 'Verifier'), ('In Process', 'In Process'), ('Unassigned', 'Unassigned'), ('Accepted', 'Accepted')], default='Unassigned', max_length=120),
        ),
    ]
