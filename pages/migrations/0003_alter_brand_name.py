# Generated by Django 4.0.4 on 2022-06-15 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
