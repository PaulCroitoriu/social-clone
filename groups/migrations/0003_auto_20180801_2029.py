# Generated by Django 2.0.7 on 2018-08-01 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20180801_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(blank=True, default='', max_length=3000),
        ),
    ]
