# Generated by Django 3.0.1 on 2019-12-24 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wifi', '0003_auto_20191224_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='location',
            field=models.TextField(blank=True, default=None),
        ),
    ]