# Generated by Django 2.0.5 on 2021-12-29 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20211220_1001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='anons',
        ),
    ]
