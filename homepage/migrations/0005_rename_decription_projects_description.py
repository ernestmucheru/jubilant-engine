# Generated by Django 3.2.5 on 2021-07-19 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_alter_projects_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='decription',
            new_name='description',
        ),
    ]