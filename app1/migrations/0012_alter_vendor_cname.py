# Generated by Django 3.2.13 on 2022-07-09 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_auto_20220709_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='cname',
            field=models.CharField(max_length=30),
        ),
    ]