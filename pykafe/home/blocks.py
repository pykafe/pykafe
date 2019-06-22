from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class PykafeRichBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(help_text='lsknlknflknlas dlajs lajs lajs f')
    align = blocks.ChoiceBlock(choices=(
               ('left', 'Left'), ('right', 'Right'),
               ('center', 'Center'), ('justify', 'Justify')),
               required=True, default=('left', 'Left')
     )

    class Meta:
        template = 'home/blocks/pykafe_rich_block.html'


class BlogRichBlock(blocks.StructBlock):
    """Blog with image and text button(s)"""
    title = blocks.CharBlock(required=True, help_text="Add your title")
    blogs = blocks.ListBlock(
               blocks.PageChooserBlock(target_model="home.BasePage", help_text='If your page does not have both an image and a description it will not show up!')
    )

    class Meta:
        template = 'home/blocks/blog_rich_block.html'
        icon = "placeholder"
        label = "Add activities"


class PykafeMap(blocks.StructBlock):
    title = blocks.CharBlock(help_text='Enter the title of the map')
    location_lat = blocks.DecimalBlock(max_value=90, min_value=-90, max_digits=15)
    location_long = blocks.DecimalBlock(max_value=180, min_value=-180, max_digits=15)
    zoom = blocks.DecimalBlock(max_value=21, min_value=0)

    class Meta:
        template = 'home/blocks/pykafe_map.html'
