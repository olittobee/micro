# Generated by Django 4.0.4 on 2022-06-05 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_book', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='topic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_book.topic'),
            preserve_default=False,
        ),
    ]