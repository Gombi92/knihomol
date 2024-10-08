# Generated by Django 5.1.1 on 2024-09-29 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authors',
            name='birth_date',
        ),
        migrations.AddField(
            model_name='authors',
            name='birth_year',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='authors',
            name='nationality',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='authors',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='authors',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
