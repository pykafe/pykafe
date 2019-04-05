from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class PykafeRichBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(help_text='lsknlknflknlas dlajs lajs lajs f')
    align = blocks.ChoiceBlock(choices=(('left','Left'), ('right', 'Right'), ('center', 'Center'), ('justify', 'Justify')), required=True, default=('left', 'Left'))

    class Meta:
        template = 'home/blocks/pykafe_rich_block.html'


class blogRichBlock(blocks.StructBlock):
    """Blog with image and text button(s)"""
    title = blocks.CharBlock(required=True, help_text="Add your title")
    blogs = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=22)),
                ("image", ImageChooserBlock(required=True)),
                ("text", blocks.TextBlock(required=True, max_length=400)),
                ("button_Page", blocks.PageChooserBlock(required=False)),
            ]
        )
    )

    class Meta:
        template = 'home/blocks/blog_rich_block.html'
        icon = "placeholder"
        label = "Add activities"
