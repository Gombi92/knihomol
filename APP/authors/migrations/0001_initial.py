# Generated by Django 5.1.1 on 2024-09-19 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('birth_year', models.SmallIntegerField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, max_length=3, null=True)),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
                'db_table': 'authors',
            },
        ),
    ]
