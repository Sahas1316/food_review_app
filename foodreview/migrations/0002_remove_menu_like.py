# Generated by Django 3.1.3 on 2020-12-12 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodreview', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='like',
        ),
    ]
