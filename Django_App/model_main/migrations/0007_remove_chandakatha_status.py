# Generated by Django 3.0.4 on 2020-03-16 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model_main', '0006_chandakatha_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chandakatha',
            name='status',
        ),
    ]
