# Generated by Django 2.1.8 on 2019-05-26 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='url',
            new_name='slug',
        ),
    ]
