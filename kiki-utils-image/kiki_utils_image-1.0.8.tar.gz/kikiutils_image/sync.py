import io

from kikiutils.decorators import try_and_get_data
from kikiutils.check import isbytes
from kikiutils.file import get_file_mime, save_file_as_bytesio
from kikiutils.requests import get_response
from PIL import Image

from .typehint import ImageData


__all__ = [
    'convert_image',
    'get_image'
]


def convert_image(
    image_data: ImageData,
    format: str = 'webp',
    quality: int = 100,
    get_bytes: bool = False
):
    """Convert image to other format, return bytes or BytesIO object."""

    if isbytes(image_data):
        image_data = io.BytesIO(image_data)
    image = Image.open(image_data)

    return save_file_as_bytesio(
        image.save,
        get_bytes,
        format=format,
        quality=quality,
        lossless=False
    )


@try_and_get_data
def get_image(
    url: str,
    check: bool = True,
    get_bytes: bool = False,
    request_method: str = 'GET'
):
    """Get image by url, return bytes or BytesIO object."""

    if (response := get_response(url, request_method)) is None:
        return

    image_bytes = response.content

    if check:
        image_mime = get_file_mime(image_bytes)

        if image_mime[0] != 'image':
            return

    if get_bytes:
        return image_bytes

    return io.BytesIO(image_bytes)
