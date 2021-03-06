# Generated by Django 3.0.5 on 2020-06-06 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_notice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='details',
            field=models.TextField(help_text='Details about notice', max_length=1000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='post',
            field=models.CharField(choices=[('Manager', 'Manager'), ('Staff', 'Staff'), ('Admin', 'Admin')], max_length=20),
        ),
    ]
