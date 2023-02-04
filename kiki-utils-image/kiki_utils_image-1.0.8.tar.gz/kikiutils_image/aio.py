from asyncio import get_event_loop

from .sync import convert_image, get_image
from .typehint import ImageData


__all__ = [
    'aconvert_image',
    'aget_image'
]


async def aconvert_image(
    image_data: ImageData,
    format: str = 'webp',
    quality: int = 100,
    get_bytes: bool = False
):
    loop = get_event_loop()
    return await loop.run_in_executor(
        None,
        convert_image,
        image_data,
        format,
        quality,
        get_bytes
    )


async def aget_image(
    url: str,
    check: bool = True,
    get_bytes: bool = False,
    request_method: str = 'GET'
):
    loop = get_event_loop()
    return await loop.run_in_executor(
        None,
        get_image,
        url,
        check,
        get_bytes,
        request_method
    )
