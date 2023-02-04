#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2023/2/1 18:14
# @Author : Rongrui Zhan
# @desc : 本代码未经授权禁止商用
from __future__ import annotations
import uvloop
import asyncio
import requests
import json
from typing import TYPE_CHECKING
from bonetools.trigger import ClipBoardTrigger

if TYPE_CHECKING:
    from typing import Any, Callable

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


def mathpix(src):
    default_headers = {
        'app_id': 'rrzhan_stu_xidian_edu_cn_c820a4',
        'app_key': 'f457c19f7c81e894fa28',
        'Content-type': 'application/json'
    }
    res = requests.post(
        'https://api.mathpix.com/v3/text',
        data=json.dumps({
            "src": src,
            "data_options": {
                "math_inline_delimiters": True,
                "include_latex": True
            }
        }), headers=default_headers)

    print(res)


def print_clip(event):
    print(ImageGrab.grabclipboard())
    print(event)


if __name__ == '__main__':
    from PIL import ImageGrab, Image


    # import keyboard
    t = ClipBoardTrigger(0.1)


    async def main():
        await asyncio.gather(*[t.async_event_loop(print_clip) for _ in range(1)])


    asyncio.run(main())
