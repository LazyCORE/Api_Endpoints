# Generated by Django 4.0.5 on 2022-06-24 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slag', models.CharField(max_length=128)),
                ('number_sort', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Напрямки',
                'verbose_name_plural': 'Напрямки',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slag', models.CharField(max_length=128)),
                ('direction', models.TextField(blank=True, default=None, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('experience', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('number_sort', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Лікарі',
                'verbose_name_plural': 'Лікарі',
            },
        ),
    ]