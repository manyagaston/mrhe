# Generated by Django 4.1.1 on 2022-11-19 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page_ministere', '0002_rename_minspage_administrationpage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administrationpage',
            name='image',
        ),
    ]