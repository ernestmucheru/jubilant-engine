# Generated by Django 3.2.5 on 2021-07-19 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20210719_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
