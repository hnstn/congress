# Generated by Django 2.1.7 on 2019-03-26 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190326_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ieee_member',
            field=models.BooleanField(default=False, verbose_name='I am an IEEE Member'),
        ),
    ]
