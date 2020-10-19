# Generated by Django 3.1.1 on 2020-10-19 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IIT_OpenOCR', '0011_auto_20201017_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='user_sets',
        ),
        migrations.AddField(
            model_name='sets',
            name='v1_rating',
            field=models.IntegerField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=0, null=True),
        ),
        migrations.AddField(
            model_name='sets',
            name='v2_rating',
            field=models.IntegerField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=0, null=True),
        ),
        migrations.AddField(
            model_name='sets',
            name='v3_rating',
            field=models.IntegerField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sets',
            name='status',
            field=models.CharField(choices=[('Set OCRed', 'Set OCRed'), ('Corrector', 'Correcctor'), ('Verifier', 'Verifier'), ('In Process', 'In Process'), ('Unassigned', 'Unassigned'), ('Accepted', 'Accepted')], default='Unassigned', max_length=120),
        ),
        migrations.DeleteModel(
            name='SetStatus',
        ),
    ]
