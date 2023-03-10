# Generated by Django 4.1.1 on 2022-11-23 12:04

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepage_description_adm_homepage_body_adm_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='content',
            field=wagtail.fields.StreamField([('title', wagtail.blocks.CharBlock(help_text="Ajouter le titre de l'agence ", max_length=40, required=True)), ('text', wagtail.blocks.TextBlock(max_length=255, required=True)), ('buttton_page', wagtail.blocks.PageChooserBlock(required=True)), ('button_url', wagtail.blocks.URLBlock(required=False))], default='', use_json_field=True),
            preserve_default=False,
        ),
    ]
