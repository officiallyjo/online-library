# Generated by Django 4.2.7 on 2023-12-27 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]