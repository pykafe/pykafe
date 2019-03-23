from wagtail.core import blocks

class PykafeRichBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(help_text='lsknlknflknlas dlajs lajs lajs f')
    align = blocks.ChoiceBlock(choices=(('left','Left'), ('right', 'Right'), ('center', 'Center'), ('justify', 'Justify')))

    class Meta:
        template = 'home/blocks/pykafe_rich_block.html'
