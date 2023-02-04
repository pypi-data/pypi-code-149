import asyncio

from functools import partial, wraps

from .sync import convert_image, get_image


__all__ = [
    'aconvert_image',
    'aget_image'
]


def _wrap(func):
    @wraps(func)
    async def run(*args, loop=None, executor=None, **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop()
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, pfunc)

    return run


aconvert_image = _wrap(convert_image)
aget_image = _wrap(get_image)
