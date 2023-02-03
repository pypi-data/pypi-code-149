import subprocess
import sys
from pathlib import Path
from typing import List

import requests

from a13e.exception import ProcessError
from a13e.plugin import PluginRegister
from a13e.recognizer import BaseRecognizer, RecognizeResult
from a13e.utils import resample, chdir_context, process_error_decorator
try:
    from importlib.resources import files
except ImportError:
    from importlib_resources import files

WIN_BINARY = 'ncm_base64-win.exe'
LINUX_BINARY = 'ncm_base64-linux'
MACOS_BINARY = 'ncm_base64-macos'

BINARY_FILE_NAME: str
if sys.platform.startswith('win'):
    BINARY_FILE_NAME = WIN_BINARY
elif sys.platform.startswith('linux'):
    BINARY_FILE_NAME = LINUX_BINARY
elif sys.platform.startswith('darwin'):
    BINARY_FILE_NAME = MACOS_BINARY
else:
    raise RuntimeError

BINARY_FILE_PATH = files('a13e.binary').joinpath(BINARY_FILE_NAME)


@process_error_decorator(ProcessError())
def _get_ncm_base64(audio_fp: Path):
    resolve = audio_fp.resolve()
    temp_fp = resample(resolve, sample_rate='48000')
    with chdir_context(Path(__file__).parent):
        output = subprocess.check_output(
            list(map(str, [BINARY_FILE_PATH, temp_fp])),
            stderr=subprocess.STDOUT
        )
        output_list: List[str] = output.decode().strip().splitlines()
        if temp_fp != resolve:
            temp_fp.unlink(missing_ok=True)

        base64 = output_list[-1]
        return base64


@PluginRegister.register
class NeteaseCloudMusic(BaseRecognizer):
    def recognize(self, audio_fp: Path, **kwargs) -> List[RecognizeResult]:
        header = {
            'authority': 'interface.music.163.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'chrome-extension://pgphbbekcgpfaekhcbjamjjkegcclhhd',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'none',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        }
        param = {
            'sessionId': '441df692-afea-4a54-8aff-f5f20fd34f12',
            'algorithmCode': 'shazam_v2',
            'duration': '6',
            'rawdata': _get_ncm_base64(audio_fp),
            'times': '2',
            'decrypt': '1'
        }
        result = requests.post(
            'https://interface.music.163.com/api/music/audio/match',
            headers=header,
            params=param
        ).json()
        if result['code'] != 200:
            raise requests.HTTPError
        if not (data := result['data']['result']):
            raise requests.HTTPError

        result_list: list[RecognizeResult] = []
        for datum in data:
            song = datum['song']
            result_list.append(
                RecognizeResult(
                    title=song['name'],
                    artist=[artist['name'] for artist in song['artists']],
                    album=song['album']['name'],
                    url=f'https://music.163.com/#/song?id={song["id"]}',
                    pic_url=song['album']['picUrl'],
                    recognizer_name=self.name
                )
            )
        return result_list

    @property
    def name(self) -> str:
        return 'NeteaseCloudMusic'
