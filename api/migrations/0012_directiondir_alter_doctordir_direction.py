# Generated by Django 4.0.5 on 2022-06-27 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_direction_options_alter_doctor_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DirectionDir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slag', models.CharField(max_length=128)),
                ('number_sort', models.IntegerField(default=1)),
            ],
        ),
        migrations.AlterField(
            model_name='doctordir',
            name='direction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.directiondir'),
        ),
    ]