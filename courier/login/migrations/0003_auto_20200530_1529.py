# Generated by Django 3.0.5 on 2020-05-30 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20200516_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='post',
            field=models.CharField(choices=[('Manager', 'Manager'), ('Staff', 'Staff')], max_length=20),
        ),
    ]
