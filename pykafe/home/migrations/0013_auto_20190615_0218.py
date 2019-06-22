# Generated by Django 2.1.5 on 2019-06-15 02:18

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20190615_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(help_text='lsknlknflknlas dlajs lajs lajs f')), ('align', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Center'), ('justify', 'Justify')]))])), ('map', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='enter the title of the map')), ('location_lat', wagtail.core.blocks.DecimalBlock(max_digits=5, max_value=90, min_value=-90)), ('location_long', wagtail.core.blocks.DecimalBlock(max_digits=5, max_value=180, min_value=-180))]))]),
        ),
    ]
