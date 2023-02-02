# -*- coding: utf-8 -*-
"""
注意事项：当使用enable_sscursor=True时，结果集只要没取完，
当前connect不能再执行别的sql，包括另外生成一个cursor也不行。
此时如果需要执行其他sql，请另外再生成一个连接对象(connect)。
"""

import logging
import pymysql

from mydbapi.mylog import *
# Module debugging log
log = debugf(__name__)


class DBApi(object):

    def __init__(self, db_config, auto_commit=True, dict_cursor=True, disable_warning=False, enable_sscursor=False):
        super(DBApi, self).__init__()
        self.conn = pymysql.connect(**db_config)
        self.conn.autocommit(auto_commit)

        self._dict_cursor = dict_cursor
        self._disable_warning = disable_warning
        self._enable_sscursor = enable_sscursor

        self._cursor = None

    def _get_cursor(self):
        if self._dict_cursor:
            cursor = self.conn.cursor(pymysql.cursors.SSDictCursor)\
                if self._enable_sscursor else self.conn.cursor(pymysql.cursors.DictCursor)
        else:
            cursor = self.conn.cursor(pymysql.cursors.SSCursor)\
                if self._enable_sscursor else self.conn.cursor()
        if self._disable_warning:
            cursor._defer_warnings = True
        # self._cursor.execute("SET SESSION binlog_format = 'STATEMENT'")
        return cursor

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__del__()

    def __del__(self):
        if self._cursor is not None:
            self._cursor.close()
        if self.conn is not None:
            self.conn.close()

    def close(self):
        return self.__del__()

    def get_insert_id(self):
        iid = self.conn.insert_id()
        log(logging.INFO, "last insert id = %s" % iid)
        return iid

    def _run_sql(self, sql, param=None, loglevel=logging.INFO, many=None, logparam=True):
        self._cursor = self._get_cursor()
        cmd = self._cursor.executemany if many else self._cursor.execute
        fmtsql = " ".join(x.strip() for x in sql.split('\n'))
        if logparam and param:
            log(loglevel, fmtsql % param)
        else:
            log(loglevel, fmtsql)
        rownum = cmd(sql, param)
        log(loglevel, 'affected rows:%s' % rownum)
        return rownum

    def query_one(self, sql, param=None, loglevel=logging.INFO):
        self._run_sql(sql, param, loglevel)
        r = self._cursor.fetchone()
        self._cursor.close()
        return r

    def query_many(self, sql, param=None, loglevel=logging.INFO):
        self._run_sql(sql, param, loglevel)
        r = self._cursor.fetchall()
        self._cursor.close()
        return r

    def query_batch(self, size, sql=None, param=None, loglevel=logging.INFO):
        if sql is not None:
            self._run_sql(sql, param, loglevel)
        #if self._cursor is not None:
        if self._enable_sscursor:
            r = self._cursor.fetchall()
        else:
            r = self._cursor.fetchmany(size)
        self._cursor.close()
        return r

    def modify(self, sql, param=None, loglevel=logging.INFO):
        self._run_sql(sql, param, loglevel)
        self._cursor.close()

    def modify_many(self, sql, param=None, loglevel=logging.INFO):
        self._run_sql(sql, param, loglevel, True, False)
        self._cursor.close()

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def begin(self):
        self.conn.begin()
