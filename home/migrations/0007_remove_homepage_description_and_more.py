# Generated by Django 4.1.1 on 2022-11-23 12:48

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_homepage_content_homepage_agence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='Description',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='Description_adm',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='body',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='body_adm',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='image_adm',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='sec_image',
        ),
        migrations.AddField(
            model_name='homepage',
            name='administration',
            field=wagtail.fields.StreamField([('administration', wagtail.blocks.StructBlock([('Description', wagtail.blocks.CharBlock(help_text='Ajouter la description ', max_length=40, required=True)), ('text', wagtail.blocks.TextBlock(max_length=255, required=True)), ('photo', wagtail.images.blocks.ImageChooserBlock(required=False))]))], default='', use_json_field=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepage',
            name='secrétariat',
            field=wagtail.fields.StreamField([('secretariat', wagtail.blocks.StructBlock([('Description', wagtail.blocks.CharBlock(help_text='Ajouter la description ', max_length=40, required=True)), ('text', wagtail.blocks.TextBlock(max_length=255, required=True)), ('photo', wagtail.images.blocks.ImageChooserBlock(required=False))]))], default='', use_json_field=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homepage',
            name='agence',
            field=wagtail.fields.StreamField([('cards', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text="Ajouter le titre de l'agence ", max_length=40, required=True)), ('text', wagtail.blocks.TextBlock(max_length=255, required=True)), ('buttton_page', wagtail.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.blocks.URLBlock(required=False))]))], use_json_field=True),
        ),
    ]