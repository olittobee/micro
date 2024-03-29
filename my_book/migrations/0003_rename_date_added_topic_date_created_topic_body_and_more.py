# Generated by Django 4.0.4 on 2022-05-28 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_book', '0002_rename_task_topic_rename_name_topic_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='date_added',
            new_name='date_created',
        ),
        migrations.AddField(
            model_name='topic',
            name='body',
            field=models.TextField(default='elijah'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='image',
            field=models.ImageField(blank=True, upload_to='my_book_image'),
        ),
    ]
