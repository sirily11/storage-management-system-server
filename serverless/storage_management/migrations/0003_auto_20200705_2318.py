# Generated by Django 3.0.8 on 2020-07-05 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage_management', '0002_auto_20200705_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='description',
            field=models.TextField(blank=True, default='No content here', null=True),
        ),
        migrations.AlterField(
            model_name='detailposition',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
