# -*- coding: utf-8 -*-
'''
    rssgen.version
    ~~~~~~~~~~~~~~~

    :copyright: 2013-2018, Lars Kiesow <lkiesow@uos.de>

    :license: FreeBSD and LGPL, see license.* for more details.

'''

'Version of python-rssgen represented as tuple'
version = (0, 9, 0)


'Version of python-rssgen represented as string'
version_str = '.'.join([str(x) for x in version])

version_major = version[:1]
version_minor = version[:2]
version_full = version

version_major_str = '.'.join([str(x) for x in version_major])
version_minor_str = '.'.join([str(x) for x in version_minor])
version_full_str = '.'.join([str(x) for x in version_full])
