# Generated by Django 2.1.7 on 2019-03-18 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='visible',
            field=models.BooleanField(default=False),
        ),
    ]