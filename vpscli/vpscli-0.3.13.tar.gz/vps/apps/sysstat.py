#!/usr/bin/env python
import os
import sqlite3
from typing import Tuple

import codefast as cf
import fire
import pandas as pd
import psutil
from rich import print


def get_db_file():
    db_file = '~/.vps/sysstat.db'
    db_file = os.path.expanduser(db_file)
    cf.shell('mkdir -p {}'.format(os.path.dirname(db_file)))
    cf.shell('touch {}'.format(db_file))
    return db_file


def get_cpu_percent(interval: int = 60):
    return psutil.cpu_percent(interval=interval)


def get_memory_usage() -> Tuple[float, float]:
    # return used percent and used GB
    vm = psutil.virtual_memory()
    return vm.percent, round(vm.used / 1024 / 1024 / 1024, 2)


def get_conn():
    conn = sqlite3.connect(get_db_file())
    conn.execute(
        'create table if not exists sysstat (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,cpu_percent real, memory_percent real, memory_gb real, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)'
    )
    return conn


def monitor(interval: int = 60):
    # collect data every 1 second
    memory_percent, memory_gb = get_memory_usage()
    cpu_percent = get_cpu_percent(interval)
    conn = get_conn()
    import datetime
    utc8 = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    conn.execute(
        'insert into sysstat (cpu_percent, memory_percent, memory_gb, timestamp) values (?, ?, ?, ?)',
        (cpu_percent, memory_percent, memory_gb, utc8))
    conn.execute(
        "delete from sysstat where timestamp < datetime('now', '-30 day')")
    conn.commit()


def display(topn: int = -1, upload: bool = False):
    conn = get_conn()
    df = pd.read_sql('select * from sysstat', conn)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.set_index('timestamp')
    if topn > 0:
        df = df.tail(topn)
    __draw_image(df)
    print(df.to_string())
    if upload:
        imgurl_upload('/tmp/sysstat.png')


def imgurl_upload(f: str):
    # upload to imgurl
    url = 'https://cf.ddot.cc/api/image'
    resp = cf.net.post(url, files={'file': open(f, 'rb')}).json()
    cf.info(resp['url'])


def __draw_image(df):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(16, 9))
    plt.plot(df.index, df['cpu_percent'], label='CPU_PERCENT')
    plt.plot(df.index, df['memory_percent'], label='MEMORY_PERCENT')
    plt.plot(df.index, df['memory_gb'], label='MEMORY_GB')
    plt.legend()
    plt.savefig('/tmp/sysstat.png')
    plt.close()


def api():
    fire.Fire({
        'monitor': monitor,
        'm': monitor,
        'display': display,
        'd': display
    })


if __name__ == '__main__':
    api()
