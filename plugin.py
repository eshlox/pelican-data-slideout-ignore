"""
Pelican - data-slideout-ignore attribute
------------------------------------------

This plugin adds data-slideout-ignore attribute to all div elements with
"highlight" class. This attribute prevents from opening slideout menu when
someone scrolls code block horizontally on tablet/mobile.

https://github.com/Mango/slideout#data-slideout-ignore-attribute

TODO:
- Add a tests for this plugin.

"""

from __future__ import unicode_literals

from bs4 import BeautifulSoup
from pelican import signals


def content_object_init(instance):
    if instance._content is not None:
        content = instance._content
        soup = BeautifulSoup(content, 'html.parser')

        for code_block in soup.findAll('div', {'class': 'highlight'}):
            code_block.attrs.update({'data-slideout-ignore': ''})

        instance._content = soup.decode()


def register():
    signals.content_object_init.connect(content_object_init)
