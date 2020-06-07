# Generated by Django 3.0.5 on 2020-06-06 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_delete_msg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(help_text='Subject/Heading of Notice', max_length=50)),
                ('details', models.TextField(help_text='Details about notice', max_length=500)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]