# Generated by Django 4.1.1 on 2022-11-19 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0077_alter_revision_user'),
        ('wagtailimages', '0024_index_image_file_hash'),
        ('page_politiques_publiques', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PolitiquePage',
            new_name='Public_PoliciesPage',
        ),
        migrations.RenameModel(
            old_name='FichierPage',
            new_name='Single_public_policyPage',
        ),
    ]
