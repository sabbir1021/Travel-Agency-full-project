# Generated by Django 3.0.4 on 2020-04-13 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0004_auto_20200413_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('subject', models.CharField(max_length=150)),
                ('message', models.TextField()),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
