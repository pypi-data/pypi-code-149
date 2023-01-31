#!/usr/bin/env python3
import json
import os

import aiohttp
import aioredis
import arrow
import codefast as cf
import joblib
import numpy as np
import pandas as pd
import requests
from codefast.argparser import ArgParser
from pydantic import BaseModel
from redis import StrictRedis
from rich import print

from cux.jupytersql import JupyterSQL
from cux.oss import AliyunOSS
from cux.redislite import redis_cli
from cux.redo import BaseRedo
from cux.sql import (AppSlave, Dev, ExtractTestConversation, IntelligenceTable,
                     Test)
from cux.turbo import Env, Turbo

from .sql import (AppSlave, Dev, ExtractTestConversation, IntelligenceTable,
                  Test)


def url_shortener(url: str) -> str:
    host = 'http://iplc-jp2.cloudiplc.com:57850/bitly'
    js = requests.post(host, json={'url': url}).json()
    return js


def sql(arg: str):
    r_list = JupyterSQL(arg).query()
    cf.io.write(r_list, '/tmp/sqlresult.csv')
    cf.info("Export result to /tmp/sqlresult.csv")
    BOUND = 10
    for r in r_list[:BOUND]:
        print(r)
    if len(r_list) >= BOUND:
        print('...')


def pipe(cid: int):
    obj = AppSlave().transcription(cid)
    print('-' * 80 + ' Pipeline information:')
    print(obj)

    if not obj:
        cf.warning('conversation_id: {} not found from database'.format(cid))
        return

    alioss = AliyunOSS()
    audio_path = obj.audio_file_path.split('com/')[1]
    text_path = obj.trans_file_path.split('com/')[1]
    audio_url = alioss.sign(audio_path)
    audio_url = url_shortener(audio_url)
    text_url = alioss.sign(text_path)
    text_url = url_shortener(text_url)
    print('{:<21} {}'.format(' public audio path', audio_url))
    print('{:<21} {}'.format(' public text path', text_url))
    print('-' * 80 + ' Audio information:')
    os.system('uix -ai "{}"'.format(audio_url))


def ai(cid: int):
    """Get ai process info"""
    assert isinstance(cid, int), 'cid must be int'
    AppSlave().ai_process(cid)


def tag(cid: int):
    cmd = 'SELECT * FROM megaview_db.tag_engine WHERE conversation_id = {}'.format(
        cid)

    df = JupyterSQL(cmd).get_df()
    for _, row in df.iterrows():
        js = row.to_dict()
        js['context'] = json.loads(row['context'])
        js['context'].sort(key=lambda x: x['order'])
        print(js)
        print('-' * 100)


def event_depth():
    cmd = 'SELECT a.name as COMPANY, count(conversation_id) as EVENT_DEPTH FROM megaview_db.ai_process b right join organization a on a.id = b.organization_id where is_event_engine_complete = 0 group by organization_id'
    r_list = JupyterSQL(cmd).query()
    depthes = [line.split(',', 1) for line in r_list]
    depthes.sort(key=lambda x: -int(x[1]) if x[1].isdigit() else float('-inf'))
    for line in depthes:
        n, d = line
        print('{:>15} \t {:<20}'.format(d, n))


def main():
    import fire
    fire.Fire({
        'sql': sql,
        'pipe': pipe,
        'ai': ai,
        'tag': tag,
        'event_depth': event_depth,
    })
