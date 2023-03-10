# Generated by Django 4.1.1 on 2023-01-12 14:52

from django.db import migrations
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page_politiques_publiques', '0018_alter_public_policiespage_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='public_policiespage',
            name='document',
            field=wagtail.fields.StreamField([('Article', wagtail.blocks.StructBlock([('Description', wagtail.blocks.CharBlock(help_text='Ajouter la description ', max_length=40, required=True)), ('text', wagtail.blocks.TextBlock(max_length=255, required=True)), ('Document', wagtail.blocks.StreamBlock([('Ajouter', wagtail.documents.blocks.DocumentChooserBlock(required=False))], max_num=2, min_num=1))], icon='cogs'))], use_json_field=True),
        ),
    ]
