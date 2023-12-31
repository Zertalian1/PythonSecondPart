# Generated by Django 4.2.5 on 2023-09-15 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('short_name', models.CharField(max_length=10)),
                ('date_of_creation', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FCs', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('year_of_admission', models.DateField()),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myCrudApp.university')),
            ],
        ),
    ]
