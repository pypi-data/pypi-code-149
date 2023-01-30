from dataclasses import dataclass, field, asdict
from typing import Dict, List, Generic, TypeVar
from abc import ABC, abstractmethod


class StateOperations:
    SET = "SET"
    GET = "GET"
    DEL = "DEL"
    HDEL = "HDEL"
    HEXISTS = "HEXISTS"
    HGETALL = "HGETALL"
    HMGET = "HMGET"
    HVALS = "HVALS"
    HGET = "HGET"
    HSET = "HSET"
    RPUSH = "RPUSH"
    LPUSH = "LPUSH"
    LLEN = "LLEN"
    LRANGE = "LRANGE"
    LPOP = "LPOP"
    LTRIM = "LTRIM"
    LINSERT = "LINSERT"
    LINDEX = "LINDEX"
    LSET = "LSET"
    LREM = "LREM"
    INCRBY = "INCRBY"
    DECRBY = "DECRBY"
    RPOP = "RPOP"
    EXPIRE = "EXPIRE"
    HLEN = "HLEN"
