# Generated by Django 2.2.6 on 2019-10-31 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos'),
        ),
    ]
