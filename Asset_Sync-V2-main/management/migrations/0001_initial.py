# Generated by Django 5.0.7 on 2024-08-09 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_joining', models.DateField()),
                ('employee_id', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('branch', models.CharField(max_length=100)),
                ('work_location', models.CharField(max_length=255)),
                ('reporting_officer', models.CharField(max_length=255)),
                ('personal_email_id', models.EmailField(max_length=254)),
            ],
        ),
    ]