# Generated by Django 4.1.1 on 2022-12-29 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_secretariat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secretariat',
            name='image',
        ),
        migrations.RemoveField(
            model_name='secretariat',
            name='page',
        ),
        migrations.DeleteModel(
            name='admin',
        ),
        migrations.DeleteModel(
            name='Secretariat',
        ),
    ]
