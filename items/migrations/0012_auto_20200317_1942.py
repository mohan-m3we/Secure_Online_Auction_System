# Generated by Django 3.0.3 on 2020-03-17 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0011_item_bidderid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='highest_bidder',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]