# Generated by Django 5.1.1 on 2024-09-14 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CarInfomation',
            new_name='CarInfo',
        ),
        migrations.RenameField(
            model_name='carinfo',
            old_name='marketTim',
            new_name='marketTime',
        ),
    ]
