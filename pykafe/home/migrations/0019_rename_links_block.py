# Generated by Django 2.1.5 on 2019-06-22 02:55

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_map_block1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basepage',
            name='body',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock(help_text='WYSIWYG text')), ('align', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Center'), ('justify', 'Justify')]))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock(help_text='WYSIWYG text')), ('align', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Center'), ('justify', 'Justify')]))])), ('links', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add your title', required=True)), ('pages', wagtail.blocks.ListBlock(wagtail.blocks.PageChooserBlock(help_text='If your page does not have both an image and a description it will not show up!', target_model=['home.BasePage'])))])), ('map', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Enter the title of the map')), ('location_lat', wagtail.blocks.DecimalBlock(max_digits=15, max_value=90, min_value=-90)), ('location_long', wagtail.blocks.DecimalBlock(max_digits=15, max_value=180, min_value=-180)), ('zoom', wagtail.blocks.DecimalBlock(max_value=21, min_value=0))]))]),
        ),
    ]
