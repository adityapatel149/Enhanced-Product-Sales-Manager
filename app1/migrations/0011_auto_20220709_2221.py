# Generated by Django 3.2.13 on 2022-07-09 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_auto_20220709_1847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='first',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='last',
        ),
        migrations.AddField(
            model_name='vendor',
            name='cname',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='pro',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.vendor'),
        ),
    ]
