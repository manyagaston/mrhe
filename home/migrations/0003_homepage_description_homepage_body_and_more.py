# Generated by Django 4.1.1 on 2022-11-19 16:06

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('home', '0002_secretariat'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='Description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepage',
            name='sec_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.DeleteModel(
            name='Secretariat',
        ),
    ]