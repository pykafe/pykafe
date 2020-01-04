# Generated by Django 2.2.5 on 2020-01-04 04:16

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20191227_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learncontentpage',
            name='body',
            field=wagtail.core.fields.StreamField([('Pages', wagtail.core.blocks.StructBlock([('languages', wagtail.core.blocks.ChoiceBlock(choices=[('tet', 'Tetum'), ('en', 'English'), ('pt', 'Portugues')])), ('pages', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock(help_text='Add your page in here', page_type=['home.SubLearnContentPage'])))], blank=True, null=True))]),
        ),
    ]
