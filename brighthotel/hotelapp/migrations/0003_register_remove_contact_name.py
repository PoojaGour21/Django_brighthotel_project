# Generated by Django 4.2.4 on 2023-10-04 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0002_customer_alter_contact_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('mobile_number', models.BigIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
    ]
