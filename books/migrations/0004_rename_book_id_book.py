# Generated by Django 4.1.4 on 2023-01-05 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_rename_book_book_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book_id',
            new_name='Book',
        ),
    ]
