# Generated by Django 4.0.4 on 2022-04-19 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_alter_exercise_muscles'),
        ('reviews', '0002_alter_review_exercise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='exercises.exercise'),
        ),
    ]