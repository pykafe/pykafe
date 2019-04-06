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
               blocks.PageChooserBlock(target_model ="home.BasePage")
    )

    class Meta:
        template = 'home/blocks/blog_rich_block.html'
        icon = "placeholder"
        label = "Add activities"
