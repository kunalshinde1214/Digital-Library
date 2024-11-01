# Generated by Django 5.1.2 on 2024-10-28 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('FICTION', 'Fiction'), ('NONFICTION', 'Non-Fiction'), ('SCIENCE', 'Science'), ('TECH', 'Technology'), ('BUSINESS', 'Business'), ('MYSTERY', 'Mystery'), ('ROMANCE', 'Romance'), ('SCIFI', 'Science Fiction'), ('FANTASY', 'Fantasy'), ('HORROR', 'Horror'), ('BIOGRAPHY', 'Biography'), ('HISTORY', 'History'), ('POETRY', 'Poetry'), ('DRAMA', 'Drama'), ('OTHER', 'Other')], default='FICTION', max_length=20),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(choices=[('EN', 'English'), ('SA', 'Sanskrit'), ('MR', 'Marathi'), ('DE', 'German'), ('CO', 'Computer'), ('OTHER', 'Other')], default='EN', max_length=10),
        ),
    ]
