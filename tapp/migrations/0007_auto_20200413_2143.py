# Generated by Django 3.0.4 on 2020-04-13 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0006_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='mark',
            field=models.FloatField(),
        ),
    ]
