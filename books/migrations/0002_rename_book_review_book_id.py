# Generated by Django 4.1.4 on 2023-01-05 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='book',
            new_name='book_id',
        ),
    ]