# Generated by Django 5.1.2 on 2024-10-28 06:11

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('language', models.CharField(choices=[('EN', 'English'), ('ES', 'Spanish'), ('FR', 'French'), ('DE', 'German'), ('IT', 'Italian'), ('OTHER', 'Other')], default='EN', max_length=10)),
                ('release_date', models.DateField()),
                ('summary', models.TextField()),
                ('file', models.FileField(upload_to='books/')),
                ('file_type', models.CharField(max_length=10)),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='library.author')),
            ],
            options={
                'ordering': ['-upload_date'],
            },
        ),
    ]
