# Generated by Django 4.2.1 on 2023-05-21 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0003_rename_name_userdb_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdb',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='userdb',
            name='Mobile',
        ),
    ]
