# Generated by Django 4.0.4 on 2022-05-28 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_book', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='Topic',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='name',
            new_name='title',
        ),
    ]