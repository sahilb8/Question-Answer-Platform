# Generated by Django 2.2.6 on 2019-11-04 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_auto_20191104_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=25),
        ),
    ]
