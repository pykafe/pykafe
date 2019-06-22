# Generated by Django 2.1.5 on 2019-06-22 02:04

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20190406_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(help_text='lsknlknflknlas dlajs lajs lajs f')), ('align', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Center'), ('justify', 'Justify')]))])), ('blog', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('blogs', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock(help_text='If your page does not have both an image and a description it will not show up!', target_model=['home.BasePage'])))])), ('map', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='enter the title of the map')), ('location_lat', wagtail.core.blocks.DecimalBlock(max_digits=15, max_value=90, min_value=-90)), ('location_long', wagtail.core.blocks.DecimalBlock(max_digits=15, max_value=180, min_value=-180)), ('zoom', wagtail.core.blocks.DecimalBlock(max_value=21, min_value=0))]))]),
        ),
    ]
