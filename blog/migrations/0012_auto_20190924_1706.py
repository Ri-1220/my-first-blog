# Generated by Django 2.0.13 on 2019-09-24 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190924_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='time2',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='time3',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='time4',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='time5',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='train2',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='train3',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='train4',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='train5',
        ),
    ]
