# Generated by Django 3.0.5 on 2020-06-07 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier_branch', '0009_auto_20200607_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daybook',
            name='branch',
            field=models.CharField(max_length=30),
        ),
    ]
