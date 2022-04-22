# Generated by Django 4.0.4 on 2022-04-21 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Muscle',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.CharField(blank=True, max_length=2000)),
                ('level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                 related_name='exercises', to='exercises.level')),
                ('muscles', models.ManyToManyField(blank=True,
                 related_name='exercises', to='exercises.muscle')),
            ],
        ),
    ]
