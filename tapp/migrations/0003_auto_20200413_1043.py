# Generated by Django 3.0.4 on 2020-04-13 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0002_articalecontact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articalecontact',
            old_name='post_contact',
            new_name='message',
        ),
    ]
