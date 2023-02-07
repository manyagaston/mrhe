# Generated by Django 4.1.1 on 2022-11-23 13:59

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_homepage_secretariat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='Secretariat',
            field=wagtail.fields.StreamField([('secretariats', wagtail.blocks.StructBlock([('Description', wagtail.blocks.CharBlock(help_text='Ajouter la description ', max_length=40, required=True)), ('text', wagtail.blocks.TextBlock(max_length=400, required=True)), ('photo', wagtail.images.blocks.ImageChooserBlock(required=False))], icon='edit'))], use_json_field=True),
        ),
    ]
