# Generated by Django 2.2.2 on 2019-07-07 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage_management', '0007_auto_20190624_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='qr_code',
            field=models.CharField(blank=True, max_length=10008, null=True),
        ),
    ]
