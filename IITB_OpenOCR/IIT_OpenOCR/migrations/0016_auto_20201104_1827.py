# Generated by Django 2.2 on 2020-11-04 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IIT_OpenOCR', '0015_auto_20201019_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sets',
            name='repoistorylink',
        ),
        migrations.AddField(
            model_name='sets',
            name='repoistoryName',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
