# Generated by Django 4.1.1 on 2022-11-19 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0077_alter_revision_user'),
        ('wagtailimages', '0024_index_image_file_hash'),
        ('page_patrimoine', '0003_detailpage_titre_ancre'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PatrimoinePage',
            new_name='National_heritagePage',
        ),
    ]
