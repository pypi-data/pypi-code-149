# Copyright (c) 2023 nggit

import asyncio

from .parsed import ParseHeader
from .http_request import HTTPRequest
from .http_response import HTTPResponse

class TremoloProtocol(asyncio.Protocol):
    def __init__(self, *args, **kwargs):
        self._options = kwargs
        self._transport = None
        self._queue = {0: None, 1: None}

        if 'loop' in kwargs:
            self._loop = kwargs['loop']
        else:
            self._loop = asyncio.get_event_loop()

    @property
    def loop(self):
        return self._loop

    @property
    def options(self):
        return self._options

    @property
    def transport(self):
        return self._transport

    @property
    def queue(self):
        return self._queue

    def connection_made(self, transport):
        self._transport = transport
        self._queue = {
            0: asyncio.Queue(),
            1: asyncio.Queue()
        }
        self._data = bytearray()
        self._body_size = 0
        self._tasks = []
        self._cancel_receive_timeout = self._loop.create_future()

        self._tasks.append(self._loop.create_task(self._receive_timeout()))

    async def _receive_timeout(self):
        _, pending = await asyncio.wait([self._cancel_receive_timeout], timeout=30)

        if pending:
            for task in pending:
                task.cancel()

            if self._transport is not None:
                print('request timeout')
                self._transport.abort()

    async def _put_to_queue(self, data, queue=None, transport=None, rate=1048576, buffer_size=16 * 1024):
        data_size = len(data)

        if (data_size >= 2 * buffer_size):
            mv = memoryview(data)

            while mv and queue is not None:
                queue.put_nowait(mv[:buffer_size].tobytes())
                await asyncio.sleep(1 / (rate / max(queue.qsize(), 1) / mv[:buffer_size].nbytes))
                mv = mv[buffer_size:]

        elif data != b'' and queue is not None:
            queue.put_nowait(data)
            await asyncio.sleep(1 / (rate / max(queue.qsize(), 1) / data_size))

        if transport is not None:
            self._body_size += data_size

            if self._body_size == self._request.content_length:
                self._queue[0].put_nowait(None)
            elif self._body_size < self._options['client_max_body_size']:
                transport.resume_reading()
            else:
                transport.write(b'HTTP/%s 413 Payload Too Large\r\nConnection: close\r\n\r\n' % self._request.version)

                if self._queue[1] is not None:
                    self._queue[1].put_nowait(None)

    async def body_received(self, request, response):
        return

    async def header_received(self, request, response):
        return

    async def _handle_request_header(self, data, sep):
        del self._data

        header = ParseHeader(data, excludes=[b'proxy'])

        if header.is_request:
            self._request = HTTPRequest(self, header)
            self._response = HTTPResponse(self, self._request)

            if self._request.method in (b'POST', b'PUT', b'PATCH'):
                if b'content-type' in self._request.headers:
                    self._request.content_type = self._request.headers[b'content-type']

                if b'content-length' in self._request.headers:
                    self._request.content_length = int(self._request.headers[b'content-length'])

                if b'expect' in self._request.headers and self._request.headers[b'expect'] == b'100-continue':
                    if self._request.content_length > self._options['client_max_body_size']:
                        if self._queue[1] is not None:
                            self._queue[1].put_nowait(
                                b'HTTP/%s 417 Expectation Failed\r\nConnection: close\r\n\r\n' % self._request.version
                            )
                            self._queue[1].put_nowait(None)

                        return
                    elif self._queue[1] is not None:
                        self._queue[1].put_nowait(b'HTTP/%s 100 Continue\r\n\r\n' % self._request.version)
                elif self._request.content_length > self._options['client_max_body_size']:
                    if self._queue[1] is not None:
                        self._queue[1].put_nowait(
                            b'HTTP/%s 413 Payload Too Large\r\nConnection: close\r\n\r\n' % self._request.version
                        )
                        self._queue[1].put_nowait(None)

                    return

                await self._put_to_queue(
                    data[sep + 4:], queue=self._queue[0], transport=self._transport, rate=self._options['upload_rate']
                )
                await self.body_received(self._request, self._response)

            await self.header_received(self._request, self._response)
        else:
            if self._queue[1] is not None:
                self._queue[1].put_nowait(None)

    def data_received(self, data):
        if hasattr(self, '_data'):
            self._data.extend(data)
            sep = self._data.find(b'\r\n\r\n')

            if sep > -1 and sep < 8192:
                    self._transport.pause_reading()
                    self._cancel_receive_timeout.set_result(None)

                    for task in (self._handle_request_header(self._data, sep), self._transfer_data()):
                        self._tasks.append(self._loop.create_task(task))
            elif sep > 8192:
                print('request header too large')
                self._transport.abort()
            elif not (sep == -1 and len(self._data) < 8192):
                print('bad request')
                self._transport.abort()

            return

        self._transport.pause_reading()
        self._tasks.append(self._loop.create_task(
            self._put_to_queue(data, queue=self._queue[0], transport=self._transport, rate=self._options['upload_rate'])
        ))

    def eof_received(self):
        if self._queue[0] is not None:
            self._queue[0].put_nowait(None)

    async def _transfer_data(self):
        while True:
            data = await self._queue[1].get()

            try:
                if data is None:
                    if self._transport.can_write_eof():
                        self._transport.write_eof()

                    self._queue[1].task_done()
                    self._transport.close()
                    return

                self._transport.write(data)
                self._queue[1].task_done()
            except Exception:
                if self._transport is not None:
                    self._transport.abort()

                if self._queue[1] is not None:
                    self._queue[1].task_done()

                return

    def connection_lost(self, exc):
        for task in self._tasks:
            try:
                if task.exception():
                    task.print_stack()
            except asyncio.base_futures.InvalidStateError:
                task.cancel()

        if hasattr(self, '_data'):
            del self._data

        self._transport = None
        self._queue = {0: None, 1: None}
