# Generated by Django 4.1.1 on 2022-11-25 01:15

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_single_postpage_bod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='single_postpage',
            name='bod',
        ),
        migrations.AlterField(
            model_name='single_postpage',
            name='body',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())], use_json_field=True),
        ),
    ]
