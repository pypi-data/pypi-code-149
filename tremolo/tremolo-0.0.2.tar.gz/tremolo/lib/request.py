# Copyright (c) 2023 nggit

import asyncio

class Request:
    def __init__(self, protocol):
        self._protocol = protocol
        self._loop = self._protocol.loop

    async def read_timeout(self):
        return

    async def _read_timeout(self, cancel_read_timeout):
        _, pending = await asyncio.wait([cancel_read_timeout], timeout=30)

        if pending:
            for task in pending:
                task.cancel()

            if self._protocol.queue[1] is not None:
                await self.read_timeout()
                self._protocol.queue[1].put_nowait(None)

    async def read(self):
        cancel_read_timeout = self._loop.create_future()
        self._loop.create_task(self._read_timeout(cancel_read_timeout))

        data = await self._protocol.queue[0].get()
        self._protocol.queue[0].task_done()
        cancel_read_timeout.set_result(None)

        if data is None:
            raise StopAsyncIteration

        yield data
