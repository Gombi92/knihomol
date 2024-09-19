# Generated by Django 5.1.1 on 2024-09-19 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('books_name', models.CharField(max_length=150)),
                ('year_of_publication', models.IntegerField(blank=True, null=True)),
                ('reading_progress', models.CharField(blank=True, choices=[('Read', 'Read'), ('Unread', 'Unread'), ('In progress', 'In progress')], max_length=12, null=True)),
                ('books_condition', models.CharField(blank=True, choices=[('a', 'Excellent'), ('b', 'Good'), ('c', 'Poor')], max_length=1, null=True)),
                ('number_of_pages', models.SmallIntegerField(blank=True, null=True)),
                ('language', models.CharField(default='čeština', max_length=50)),
                ('book_type', models.CharField(blank=True, choices=[('E-book', 'E-book'), ('Physical', 'Physical')], max_length=8, null=True)),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'db_table': 'books',
            },
        ),
    ]
