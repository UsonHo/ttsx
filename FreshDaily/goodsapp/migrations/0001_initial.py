# Generated by Django 2.2.4 on 2019-10-30 10:54

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ttitle', models.CharField(max_length=10)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gtitle', models.CharField(max_length=20)),
                ('gpic', models.ImageField(upload_to='goodsPic')),
                ('gprice', models.DecimalField(decimal_places=2, max_digits=7)),
                ('isDelete', models.BooleanField(default=False)),
                ('gunit', models.CharField(default='500g', max_length=10)),
                ('gclick', models.IntegerField()),
                ('gbrief', models.CharField(max_length=100)),
                ('gstock', models.IntegerField()),
                ('gcount', tinymce.models.HTMLField()),
                ('gtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goodsapp.GoodsInfo')),
            ],
        ),
    ]
