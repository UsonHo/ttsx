# Generated by Django 2.2.4 on 2019-10-30 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodsapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goodsinfo',
            old_name='gcount',
            new_name='gcontent',
        ),
    ]