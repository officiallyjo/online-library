# Generated by Django 4.2.7 on 2023-12-27 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_book_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='time_posted',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
