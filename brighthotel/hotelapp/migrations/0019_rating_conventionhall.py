# Generated by Django 4.2.4 on 2023-11-16 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0018_remove_rating_conventionhall'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='conventionhall',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hotelapp.conventionhall'),
            preserve_default=False,
        ),
    ]
