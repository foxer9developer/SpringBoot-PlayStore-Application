# Generated by Django 3.1.1 on 2020-12-17 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IIT_OpenOCR', '0021_auto_20201217_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_status',
            field=models.CharField(choices=[('Available', 'Idle'), ('Assigned', 'Assigned')], default='Idle', max_length=80),
        ),
    ]
