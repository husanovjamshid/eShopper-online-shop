# Generated by Django 4.0.4 on 2022-06-18 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_remove_product_mavjud_product_soni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='soni',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
