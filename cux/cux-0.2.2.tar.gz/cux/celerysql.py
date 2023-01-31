#!/usr/bin/env python
from func_timeout import func_timeout, FunctionTimedOut

import codefast as cf
import pandas as pd
import pymysql
from pyserverless.apps.rabbitmq import Consumer, Publisher
from redis import StrictRedis
# from cux.auth import OnlineAuth
from celery import Celery

broker= 'redis://:DdLC7rycmRDfRY@cn.ddot.cc:15672/0'
app = Celery('eloop', broker=broker, backend=broker)

app.conf.result_expires = 10

@app.task
def execute_sql(query:str) -> pd.DataFrame:
    conn = pymysql.connect(
        host="172.18.54.40",
        user="developer",
        passwd="Hq)%33K7HpJGHaavV",
        db="megaview_db",
        port=6447,
    )
    try:
        data = func_timeout(30, pd.read_sql_query, args=(query, conn))
        return data
    except FunctionTimedOut:
        cf.info("could not complete within finite seconds, hence terminated.")
        return ""
    except Exception as e:
        return str(e)

