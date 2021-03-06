# Generated by Django 3.1.1 on 2020-09-14 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IIT_OpenOCR', '0002_auto_20200914_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='avg_rating',
        ),
        migrations.RemoveField(
            model_name='users',
            name='pages_completed',
        ),
        migrations.RemoveField(
            model_name='users',
            name='sets_completed',
        ),
        migrations.CreateModel(
            name='SetStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sets_completed', models.BigIntegerField(default=0)),
                ('pages_completed', models.BigIntegerField(default=0)),
                ('avg_rating', models.IntegerField(choices=[(5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], default=0)),
                ('github_username', models.ForeignKey(limit_choices_to={'user_role': 'Corrector'}, on_delete=django.db.models.deletion.PROTECT, to='IIT_OpenOCR.users', to_field='github_username')),
            ],
        ),
    ]
