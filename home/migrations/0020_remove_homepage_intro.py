# Generated by Django 4.1.1 on 2022-12-29 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_homepage_intro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='intro',
        ),
    ]
