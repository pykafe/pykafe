# Generated by Django 2.2.5 on 2020-01-16 22:18

from django.db import migrations, models
import django.db.models.deletion
import wagtail.contrib.table_block.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('home', '0022_auto_20191028_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='LearnCategory_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubLearnContentPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('body', wagtail.fields.StreamField([('category_type', wagtail.blocks.StructBlock([('category_type', wagtail.snippets.blocks.SnippetChooserBlock('home.LearnCategory_type', required=False)), ('align', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Center'), ('justify', 'Justify')]))], blank=True, null=True)), ('content', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock(help_text='Add your content in here', required=False)), ('align', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Center'), ('justify', 'Justify')]))], blank=True, null=True)), ('code', wagtail.blocks.StructBlock([('code_url', wagtail.blocks.URLBlock(label='External URL', required=False)), ('code', wagtail.blocks.StructBlock([('language', wagtail.blocks.ChoiceBlock(choices=[('css', 'CSS'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.blocks.TextBlock(identifier='code', label='Code'))], label='Source Code', language='WAGTAIL_CODE_BLOCK_LANGUAGES', required=False)), ('align', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Center'), ('justify', 'Justify')]))], blank=True, null=True)), ('table', wagtail.blocks.StreamBlock([('table', wagtail.contrib.table_block.blocks.TableBlock()), ('align', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Center'), ('justify', 'Justify')]))], blank=True, null=True))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterUniqueTogether(
            name='learnpagelearncategory',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='learnpagelearncategory',
            name='learn_category',
        ),
        migrations.RemoveField(
            model_name='learnpagelearncategory',
            name='page',
        ),
        migrations.AlterField(
            model_name='learncontentpage',
            name='body',
            field=wagtail.fields.StreamField([('Pages', wagtail.blocks.StructBlock([('languages', wagtail.blocks.ChoiceBlock(choices=[('tet', 'Tetum'), ('en', 'English'), ('pt', 'Portugues')])), ('logo_images', wagtail.images.blocks.ImageChooserBlock()), ('pages', wagtail.blocks.ListBlock(wagtail.blocks.PageChooserBlock(help_text='Add your page in here', page_type=['home.SubLearnContentPage'])))], blank=True, null=True))]),
        ),
        migrations.DeleteModel(
            name='LearnCategory',
        ),
        migrations.DeleteModel(
            name='LearnPageLearnCategory',
        ),
    ]
