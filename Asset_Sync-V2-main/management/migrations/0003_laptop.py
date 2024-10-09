# Generated by Django 5.0.7 on 2024-08-09 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_employee_exited_alter_employee_department_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('processor', models.CharField(max_length=100)),
                ('ram_capacity', models.CharField(max_length=50)),
                ('storage', models.CharField(max_length=50)),
                ('inch', models.DecimalField(decimal_places=1, max_digits=4)),
                ('status', models.CharField(max_length=50)),
                ('building_name', models.CharField(max_length=100)),
                ('date_of_purchase', models.DateField()),
                ('purchased_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('warranty_details', models.CharField(max_length=100)),
                ('warranty_date', models.DateField()),
                ('remarks', models.TextField(blank=True, null=True)),
            ],
        ),
    ]