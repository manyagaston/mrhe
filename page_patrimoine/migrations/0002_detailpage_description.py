# Generated by Django 4.1.1 on 2022-11-09 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_patrimoine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailpage',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
