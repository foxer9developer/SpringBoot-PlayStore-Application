# Generated by Django 3.1.1 on 2020-12-17 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IIT_OpenOCR', '0022_auto_20201217_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_status',
            field=models.CharField(choices=[('Available', 'Available'), ('Assigned', 'Assigned')], default='Idle', max_length=80),
        ),
    ]
