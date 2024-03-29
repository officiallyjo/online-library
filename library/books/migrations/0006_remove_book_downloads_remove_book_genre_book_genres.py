# Generated by Django 4.2.7 on 2023-12-26 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_book_downloads'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='downloads',
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(to='books.genre'),
        ),
    ]
