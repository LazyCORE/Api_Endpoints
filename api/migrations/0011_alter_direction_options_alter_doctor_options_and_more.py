# Generated by Django 4.0.5 on 2022-06-27 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_doctor_experience_doctor_years_of_experience_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='direction',
            options={'verbose_name': 'Напрямок', 'verbose_name_plural': 'Напрямки'},
        ),
        migrations.AlterModelOptions(
            name='doctor',
            options={'verbose_name': 'Лікара', 'verbose_name_plural': 'Лікарі'},
        ),
        migrations.CreateModel(
            name='DoctorDir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slag', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=128)),
                ('date', models.DateField()),
                ('years_of_experience', models.IntegerField(default=0)),
                ('number_sort', models.IntegerField(default=1)),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.direction')),
            ],
        ),
    ]
