# Generated by Django 4.2.7 on 2023-11-19 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_books_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('book', models.FileField(upload_to='pdfs')),
                ('blurb', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='book_images/')),
            ],
        ),
        migrations.DeleteModel(
            name='books',
        ),
    ]
