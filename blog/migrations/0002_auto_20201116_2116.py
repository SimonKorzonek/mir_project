# Generated by Django 3.1.3 on 2020-11-16 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='offline',
            new_name='online',
        ),
    ]
