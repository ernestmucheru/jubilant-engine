# Generated by Django 3.2.5 on 2021-07-19 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_rename_decription_projects_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Projects',
        ),
    ]
