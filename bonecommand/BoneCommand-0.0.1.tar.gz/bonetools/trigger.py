#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2023/2/1 18:05
# @Author : Rongrui Zhan
# @desc : 本代码未经授权禁止商用
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Callable
import asyncio
import pyperclip


class Trigger:
    id = "trigger.base"

    def __init__(self, interval: float = 0.01):
        self.interval = interval

    def trigger(self) -> tuple[bool, dict]:
        raise NotImplementedError

    async def async_event_loop(self, func: Callable):
        while True:
            happened, event = self.trigger()
            if happened:
                func(event)
            await asyncio.sleep(self.interval)


class ClipBoardTrigger(Trigger):
    clipboard = pyperclip.paste()


    def trigger(self):
        new = pyperclip.paste()
        if new != self.clipboard:
            self.clipboard = new
            return True, new
        return False, None
