# Generated by Django 3.2.13 on 2022-06-24 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_product_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=15)),
                ('lname', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
                ('password', models.CharField(max_length=8)),
            ],
        ),
    ]
