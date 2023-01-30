#
# Copyright (c) 2015-2020 Thierry Florac <tflorac AT ulthar.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""PyAMS_skin.schema base module

"""

__docformat__ = 'restructuredtext'

from zope.interface import implementer
from zope.schema import Bool, Choice, Dict, Object
from zope.schema.fieldproperty import FieldProperty

from pyams_skin.interfaces import BOOTSTRAP_SIZES, BOOTSTRAP_SIZES_VOCABULARY
from pyams_skin.interfaces.schema import BootstrapThumbnailSelection, IBootstrapSizeField, \
    IBootstrapThumbnailSelection, IBootstrapThumbnailsSelectionField, IBootstrapDevicesBooleanField


@implementer(IBootstrapSizeField)
class BootstrapSizeField(Choice):
    """Bootstrap size selection field"""

    def __init__(self, values=None, vocabulary=None, source=None, **kw):
        super().__init__(vocabulary=BOOTSTRAP_SIZES_VOCABULARY, **kw)


class BootstrapThumbnailSelectionField(Object):
    """Bootstrap single thumbnail selection field"""

    def __init__(self, schema=None, **kw):
        super().__init__(schema=IBootstrapThumbnailSelection, **kw)


@implementer(IBootstrapThumbnailsSelectionField)
class BootstrapThumbnailsSelectionField(Dict):
    """Bootstrap full selection dict field"""

    def __init__(self, key_type=None, value_type=None,
                 default=None, default_width=None,
                 change_width=True, **kw):
        super().__init__(key_type=BootstrapSizeField(required=True),
                         value_type=BootstrapThumbnailSelectionField(),
                         **kw)
        self.default_width = default_width
        self.change_width = change_width

    @property
    def default(self):
        return {
            size: BootstrapThumbnailSelection(cols=self.default_width)
            for size in BOOTSTRAP_SIZES.keys()
        }

    @default.setter
    def default(self, value):
        pass


@implementer(IBootstrapDevicesBooleanField)
class BootstrapDevicesBooleanField(Dict):
    """Bootstrap boolean devices field

    This field allows to define a boolean value for each Bootstrap device size.
    """

    default_value = FieldProperty(IBootstrapDevicesBooleanField['default_value'])

    def __init__(self, key_type=None, value_type=None,
                 default=True, **kw):
        super().__init__(key_type=BootstrapSizeField(required=True),
                         **kw)
        if isinstance(default, bool):
            self.default_value = {
                size: default
                for size in BOOTSTRAP_SIZES.keys()
            }
        else:
            self.default_value = default

    @property
    def default(self):
        return self.default_value

    @default.setter
    def default(self, value):
        pass
