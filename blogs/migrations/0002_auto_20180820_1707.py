# Generated by Django 2.1 on 2018-08-20 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='content',
            field=models.TextField(max_length=200),
        ),
    ]
