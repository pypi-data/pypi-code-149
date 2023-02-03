import time
from contextlib import closing
from pathlib import Path
from typing import TypedDict, List

import eyed3
import eyed3.id3
import requests
from filetype import filetype

from a13e.utils import temp_file_context


class SongData(TypedDict, total=False):
    title: str
    artist: List[str]
    album: str
    pic_url: str


def download_image(url: str):
    img_fp = Path.cwd().resolve() / str(time.time())
    with closing(requests.get(url, stream=True)) as response, open(img_fp, mode='wb') as file:
        for data in response.iter_content(128):
            file.write(data)

    return img_fp


def set_tag(mp3_fp: Path, data: 'SongData'):
    """Set tags for MP3 files, which will overwrite the original files."""
    mp3file = eyed3.load(mp3_fp)
    if mp3file.tag is None:
        mp3file.initTag()
    mp3file.tag.title = data.get('title')
    mp3file.tag.album = data.get('album')
    mp3file.tag.artist = '/'.join(data.get('artist', []))
    if pic_url := data.get('pic_url'):
        with temp_file_context(download_image(pic_url), mode='rb') as tf:
            mp3file.tag.images.set(
                eyed3.id3.frames.ImageFrame.FRONT_COVER,
                tf.read(),
                filetype.guess(tf).mime
            )
    mp3file.tag.save(version=eyed3.id3.ID3_V2_3, encoding='utf-8')
    return mp3file.tag
