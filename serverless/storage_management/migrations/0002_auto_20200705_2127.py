# Generated by Django 3.0.8 on 2020-07-05 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, help_text='Please enter your item description', null=True),
        ),
    ]
