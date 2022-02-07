"""Streamfields live in here"""
from wagtail.core import blocks

class TitleAndText(blocks.StructBlock):
    """Title and text and nothing else"""

    title = blocks.CharBlock(required=True, help_text='Add your title')
    text =  blocks.TextBlock(required=True, help_text='Add additional text')

    class Meta: 
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"