# Generated by Django 3.1.1 on 2020-10-17 04:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('IIT_OpenOCR', '0008_book_book_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sets',
            name='assignmentdate',
        ),
        migrations.RemoveField(
            model_name='sets',
            name='lastsubdate',
        ),
        migrations.AddField(
            model_name='sets',
            name='vone_assignmentdate',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='sets',
            name='vone_expsubdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='sets',
            name='vthree_assignmentdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='sets',
            name='vthree_expsubdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='sets',
            name='vtwo_assignmentdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='sets',
            name='vtwo_expsubdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='sets',
            name='finalsubdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='sets',
            name='setCorrector',
            field=models.ForeignKey(limit_choices_to={'user_role': 'Corrector'}, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='set_corrector', to='IIT_OpenOCR.users'),
        ),
        migrations.AlterField(
            model_name='sets',
            name='setVerifier',
            field=models.ForeignKey(limit_choices_to={'user_role': 'Verifier'}, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='set_verifier', to='IIT_OpenOCR.users'),
        ),
    ]