# Generated by Django 2.1.5 on 2019-04-02 11:43

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20190330_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock(help_text='lsknlknflknlas dlajs lajs lajs f')), ('align', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Center'), ('justify', 'Justify')]))])), ('blog', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add your title', required=True)), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(max_length=22, required=True)), ('text', wagtail.blocks.TextBlock(max_length=500, required=True)), ('button_Page', wagtail.blocks.PageChooserBlock(required=False))])))]))]),
        ),
    ]
