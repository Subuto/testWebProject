# Generated by Django 4.0.4 on 2022-05-03 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_factory', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='p_Cut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Motor_Torque', models.DecimalField(decimal_places=10, max_digits=19)),
                ('Lag_error', models.DecimalField(decimal_places=10, max_digits=19)),
                ('Actual_position', models.DecimalField(decimal_places=10, max_digits=19)),
                ('Actual_speed', models.DecimalField(decimal_places=10, max_digits=19)),
            ],
        ),
        migrations.CreateModel(
            name='p_Cut_analysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speed_change', models.DecimalField(decimal_places=10, max_digits=19)),
                ('replacement_history', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='p_SvoFilm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Actual_position', models.DecimalField(decimal_places=10, max_digits=19)),
                ('Actual_speed', models.DecimalField(decimal_places=10, max_digits=19)),
                ('Lag_error', models.DecimalField(decimal_places=10, max_digits=19)),
            ],
        ),
    ]