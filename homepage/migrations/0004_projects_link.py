# Generated by Django 3.2.5 on 2021-07-20 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_alter_projects_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='link',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]