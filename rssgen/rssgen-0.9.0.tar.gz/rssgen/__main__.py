# -*- coding: utf-8 -*-
'''
    rssgen
    ~~~~~~~

    :copyright: 2013-2016, Lars Kiesow <lkiesow@uos.de>

    :license: FreeBSD and LGPL, see license.* for more details.
'''

import sys

from rssgen.feed import RssGenerator


USAGE = '''
Usage: python -m rssgen [OPTION]

Use one of the following options:

File options:
  <file>.atom      -- Generate ATOM test feed
  <file>.rss       -- Generate RSS test teed
'''


def print_enc(s):
    '''Print function compatible with both python2 and python3 accepting strings
    and byte arrays.
    '''
    if sys.version_info[0] >= 3:
        print(s.decode('utf-8') if isinstance(s, bytes) else s)
    else:
        print(s)


def main():
    if len(sys.argv) != 2 or not (
            sys.argv[1].endswith('rss') or
            sys.argv[1].endswith('atom')):
        print(USAGE)
        exit()

    arg = sys.argv[1]

    fg = RssGenerator()
    fg.id('http://lernfunk.de/_MEDIAID_123')
    fg.title('Testfeed')
    fg.author({'name': 'Lars Kiesow', 'email': 'lkiesow@uos.de'})
    fg.link(href='http://example.com', rel='alternate')
    fg.category(term='test')
    fg.contributor(name='Lars Kiesow', email='lkiesow@uos.de')
    fg.contributor(name='John Doe', email='jdoe@example.com')
    fg.icon('http://ex.com/icon.jpg')
    fg.logo('http://ex.com/logo.jpg')
    fg.rights('cc-by')
    fg.subtitle('This is a cool feed!')
    fg.link(href='http://larskiesow.de/test.atom', rel='self')
    fg.language('de')
    fe = fg.add_entry()
    fe.id('http://lernfunk.de/_MEDIAID_123#1')
    fe.title('First Element')
    fe.content('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Tamen
            aberramus a proposito, et, ne longius, prorsus, inquam, Piso, si
            ista mala sunt, placet. Aut etiam, ut vestitum, sic sententiam
            habeas aliam domesticam, aliam forensem, ut in fronte ostentatio
            sit, intus veritas occultetur? Cum id fugiunt, re eadem defendunt,
            quae Peripatetici, verba.''')
    fe.summary(u'Lorem ipsum dolor sit amet, consectetur adipiscing elit…')
    fe.link(href='http://example.com', rel='alternate')
    fe.author(name='Lars Kiesow', email='lkiesow@uos.de')

    if arg == 'atom':
        print_enc(fg.atom_str(pretty=True))
    elif arg == 'rss':
        print_enc(fg.rss_str(pretty=True))
    elif arg.endswith('atom'):
        fg.atom_file(arg)
    elif arg.endswith('rss'):
        fg.rss_file(arg)


if __name__ == '__main__':
    main()
