# Generated by Django 4.1.1 on 2022-11-19 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('wagtailcore', '0077_alter_revision_user'),
        ('page_ministere', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MinsPage',
            new_name='AdministrationPage',
        ),
        migrations.RenameModel(
            old_name='PersPage',
            new_name='Single_biographyPage',
        ),
    ]
