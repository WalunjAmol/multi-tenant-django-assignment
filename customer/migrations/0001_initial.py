# Generated by Django 5.2.1 on 2025-05-21 18:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='department.department', verbose_name='Department')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
                'ordering': ['first_name', 'last_name'],
            },
        ),
    ]
