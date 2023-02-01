##############################################################################
#
# Copyright (c) 2004, 2005 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

from AccessControl.class_init import InitializeClass
from OFS.SimpleItem import SimpleItem
from zope.formlib.widget import CustomWidgetFactory
from zope.i18nmessageid import MessageFactory
from zope.interface import Interface
from zope.interface import implementer
from zope.schema import Int
from zope.schema import List
from zope.schema import Object
from zope.schema import Text
from zope.schema import TextLine

from five.formlib.objectwidget import ObjectWidget


_ = MessageFactory('formtest')


class IFieldContent(Interface):

    title = TextLine(
        title=_("Title"),
        description=_("A short description of the event."),
        default="",
        required=True
    )

    description = Text(
        title=_("Description"),
        description=_("A long description of the event."),
        default="",
        required=False
    )

    somenumber = Int(
        title=_("Some number"),
        default=0,
        required=False
    )

    somelist = List(
        title=_("Some List"),
        value_type=TextLine(title=_("Some item")),
        default=[],
        required=False
    )


@implementer(IFieldContent)
class FieldContent(SimpleItem):
    """A Viewable piece of content with fields"""
    meta_type = 'Five FieldContent'

    def __init__(self, id, title):
        self.id = id
        self.title = title


InitializeClass(FieldContent)


def manage_addFieldContent(self, id, title, REQUEST=None):
    """Add the field content"""
    id = self._setObject(id, FieldContent(id, title))
    return ''


class IComplexSchemaContent(Interface):

    fishtype = TextLine(
        title="Fish type",
        description="The type of fish",
        default="It was a lovely little fish. And it went wherever I did go.",
        required=False)

    fish = Object(
        title="Fish",
        schema=IFieldContent,
        description="The fishy object",
        required=True)


@implementer(IComplexSchemaContent)
class ComplexSchemaContent(SimpleItem):
    meta_type = "Five ComplexSchemaContent"

    def __init__(self, id):
        self.id = id
        self.fish = FieldContent('fish', 'title')
        self.fish.description = ""
        self.fishtype = 'Lost fishy'


class ComplexSchemaView:
    """Needs a docstring"""

    fish_widget = CustomWidgetFactory(ObjectWidget, FieldContent)


InitializeClass(ComplexSchemaContent)


def manage_addComplexSchemaContent(self, id, REQUEST=None):
    """Add the complex schema content"""
    id = self._setObject(id, ComplexSchemaContent(id))
    return ''


def modifiedSubscriber(content, ev):
    """A simple event handler, which sets a flag on the object"""
    content._modified_flag = True


def createdSubscriber(content, ev):
    """A simple event handler, which sets a flag on the object"""
    content._created_flag = True
