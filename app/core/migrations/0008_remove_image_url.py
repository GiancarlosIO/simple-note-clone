# Generated by Django 2.1.8 on 2019-04-14 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190414_0426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='url',
        ),
    ]