# Generated by Django 4.0.5 on 2022-06-25 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_delete_indirection_delete_indoctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='DirectionForChoose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slag', models.CharField(max_length=128)),
                ('number_sort', models.IntegerField(default=1)),
            ],
        ),
    ]