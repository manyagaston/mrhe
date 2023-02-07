# Generated by Django 4.1.1 on 2022-11-23 14:00

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_homepage_secretariat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='Secretariat',
            field=wagtail.fields.StreamField([('secretariats', wagtail.blocks.StructBlock([('Description', wagtail.blocks.CharBlock(help_text='Ajouter la description ', max_length=40, required=True)), ('text', wagtail.blocks.TextBlock(max_length=500, required=True)), ('photo', wagtail.images.blocks.ImageChooserBlock(required=False))], icon='edit'))], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='agence',
            field=wagtail.fields.StreamField([('cards', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text="Ajouter le titre de l'agence ", max_length=40, required=True)), ('text', wagtail.blocks.TextBlock(max_length=500, required=True)), ('buttton_page', wagtail.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.blocks.URLBlock(required=False))]))], use_json_field=True),
        ),
    ]