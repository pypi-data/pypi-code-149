import sys
from urllib.parse import urljoin
from EpubCrawler.util import request_retry
from pyquery import PyQuery as pq
import json

config = {
    'url': '',
    'link': '',
    'proxy': None,
    'headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    },
}

def get_toc(html, base):
    root = pq(html)
    el_links = root(config['link'])
    links = []
    for i in range(len(el_links)):
        url = el_links.eq(i).attr('href')
        if not url:
            links.append(el_links.eq(i).text().strip())
            continue
        links.append(urljoin(base, url))
    return links

def fetch_links(args):
    config['url'] = args.url
    config['link'] = args.link
    ofname = args.ofname
    st = args.start
    ed = args.end
    
    if args.proxy:
        config['proxy'] = {
            'http': args.proxy,
            'https': args.proxy,
        }
    if args.headers:
        config['headers'] = json.loads(args.headers)
    
    ofile = open(ofname, 'a', encoding='utf-8')
    
    for i in range(st, ed + 1):
        url = config['url'].replace('{i}', str(i))
        print(url)
        html = request_retry(
            'GET', url, 
            proxies=config['proxy'],
            headers=config['headers'],
        ).text
        toc = get_toc(html, url)
        if len(toc) == 0: break
        for it in toc:
            print(it)
            ofile.write(it + '\n')
    
    ofile.close()
