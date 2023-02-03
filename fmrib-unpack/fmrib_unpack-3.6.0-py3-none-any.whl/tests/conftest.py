#!/usr/bin/env python
#
# conftest.py -
#
# Author: Paul McCarthy <pauldmccarthy@gmail.com>
#

import inspect

import funpack.fileinfo         as fileinfo
import funpack.schema           as schema
import funpack.schema.hierarchy as hierarchy
import funpack.schema.coding    as coding


schema.NEVER_DOWNLOAD = True


def fake_cache_clear():
    pass


fileinfo.sniff               = inspect.unwrap(fileinfo.sniff)
fileinfo.fileinfo            = inspect.unwrap(fileinfo.fileinfo)
hierarchy._loadHierarchyFile = inspect.unwrap(hierarchy.loadHierarchyFile)
coding._loadCodingFile       = inspect.unwrap(coding._loadCodingFile)

fileinfo.sniff              .cache_clear = fake_cache_clear
fileinfo.fileinfo           .cache_clear = fake_cache_clear
hierarchy._loadHierarchyFile.cache_clear = fake_cache_clear
coding._loadCodingFile      .cache_clear = fake_cache_clear
