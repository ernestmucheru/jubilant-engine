# Generated by Django 3.2.5 on 2021-07-19 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to='')),
                ('decription', models.CharField(max_length=300)),
            ],
        ),
    ]