# Generated by Django 4.2.4 on 2023-11-16 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0015_rename_hall_rating_conventionhall'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='conventionhall',
        ),
        migrations.AddField(
            model_name='rating',
            name='mail',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
