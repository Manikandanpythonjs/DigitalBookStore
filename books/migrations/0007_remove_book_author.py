# Generated by Django 4.1.4 on 2023-01-15 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_authors_book_authorname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='Author',
        ),
    ]
