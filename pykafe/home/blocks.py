from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtailcodeblock.blocks import CodeBlock


CHOICES_ALIGN = (
        ('left', 'Left'), 
        ('right', 'Right'), 
        ('center', 'Center'), 
        ('justify', 'Justify')
)


class PykafeRichBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(help_text='Add your text in here')
    align = blocks.ChoiceBlock(choices=CHOICES_ALIGN,
               required=True, default=('left', 'Left')
     )

    class Meta:
        template = 'home/blocks/page_links_block.html'


class PageLinksBlock(blocks.StructBlock):
    """Titled list of links to pages"""
    title = blocks.CharBlock(required=True, help_text="Add your title")
    pages = blocks.ListBlock(
               blocks.PageChooserBlock(target_model="home.BasePage", help_text='If your page does not have both an image and a description it will not show up!')
    )

    class Meta:
        template = 'home/blocks/pykafe_rich_block.html'
        icon = "placeholder"


class PykafeMap(blocks.StructBlock):
    title = blocks.CharBlock(help_text='Enter the title of the map')
    location_lat = blocks.DecimalBlock(max_value=90, min_value=-90, max_digits=15)
    location_long = blocks.DecimalBlock(max_value=180, min_value=-180, max_digits=15)
    zoom = blocks.DecimalBlock(max_value=21, min_value=0)

    class Meta:
        template = 'home/blocks/pykafe_map.html'


# Kria Rich block ba category
class CategoryRichBlock(blocks.StructBlock):
    category_type = blocks.CharBlock(required=False, help_text="Add your category type")
    categories = SnippetChooserBlock('home.LearnCategory', required=False)

    class Meta:
        template = 'home/blocks/learn_rich_block.html'


# Kria Rich block ba content 
class LearnRichBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(required=False, help_text='Add your content in here')
    align = blocks.ChoiceBlock(choices=CHOICES_ALIGN,
               required=True, default=('left', 'Left')
     )
     
    class Meta:
        template = 'home/blocks/learn_rich_block.html'


# Kria Rich block ba coding 
class CodeRichBlock(blocks.StructBlock):
    code = CodeBlock(label='Bash Code', language='WAGTAIL_CODE_BLOCK_LANGUAGES', required=False)
    align = blocks.ChoiceBlock(choices=CHOICES_ALIGN,
               required=True, default=('left', 'Left')
     )

    class Meta:
        template = 'home/blocks/learn_rich_block.html'
