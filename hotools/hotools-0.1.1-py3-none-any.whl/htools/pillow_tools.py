"""Functions about Pillow
"""
from typing import Tuple

from PIL import Image, ImageDraw, ImageFont

COLOR = Tuple[int, int, int]


def _draw_str(
        draw: ImageDraw,
        font,
        message: str,
        fore_ground_color: COLOR,
        back_ground_color: COLOR,
        rect: Tuple[int, int, int, int]
):
    if back_ground_color:
        draw.rectangle(rect, fill=back_ground_color)
    draw.text((rect[0], rect[1]), message, fill=fore_ground_color, font=font)


def draw_str_at_point(
        image: Image,
        message: str,
        point: Tuple[int, int],
        font_path: str,
        font_height=32,
        fore_ground_color=(0, 0, 0),
        back_ground_color=None
):
    image_width, image_height = image.size
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_height)
    message_width, message_height = draw.textsize(message, font)

    rect = (point[0], point[1], point[0] + message_width, point[1] + font_height)
    _draw_str(draw, font, message, fore_ground_color, back_ground_color, rect)


def draw_str_at_center(
        image: Image,
        message: str,
        font_path: str,
        font_height=32,
        fore_ground_color=(0, 0, 0),
        back_ground_color=None
):
    image_width, image_height = image.size
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_height)
    message_width, message_height = draw.textsize(message, font)

    rect = (image_width * 0.5 - (message_width * 0.5),
            image_height * 0.5 - font_height * 0.5,
            image_width * 0.5 + (message_width * 0.5),
            image_height * 0.5 + font_height * 0.5)
    _draw_str(draw, font, message, fore_ground_color, back_ground_color, rect)
