# Generated by Django 5.1.6 on 2025-03-05 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='users',
            new_name='user',
        ),
    ]
