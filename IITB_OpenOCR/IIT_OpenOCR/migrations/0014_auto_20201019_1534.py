# Generated by Django 3.1.1 on 2020-10-19 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IIT_OpenOCR', '0013_users_user_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sets',
            old_name='deadline',
            new_name='vone_deadline',
        ),
        migrations.AddField(
            model_name='sets',
            name='vthree_deadline',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sets',
            name='vtwo_deadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]