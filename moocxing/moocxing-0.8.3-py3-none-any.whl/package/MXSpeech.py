import ffmpeg
from aip.speech import AipSpeech
from moocxing.robot import Constants
import logging

log = logging.getLogger(__name__)


class MXSpeech:
    def __init__(self, APP_ID, API_KEY, SECRET_KEY):
        self.client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    def TTS(self, text, path=Constants.PATH_TEMP_MP3):
        """文本转语音"""
        result = self.client.synthesis(text, 'zh', 4, {'vol': 5, 'per': 4, })
        if not isinstance(result, dict):
            with open(path, 'wb') as f:
                f.write(result)

        ffmpeg.run(ffmpeg.output(
            ffmpeg.input(path), path.replace('mp3', 'wav')),
            quiet=True,
            overwrite_output=True
        )

    def STT(self, path=Constants.PATH_TEMP_WAV, _print=False):
        """语音转文本"""
        with open(path, 'rb') as fp:
            data = fp.read()

        result = self.client.asr(data, 'pcm', 16000, {'dev_pid': 1537, })
        if result['err_no'] == 0:
            if _print:
                log.info(result['result'][0])
            return str(result['result'][0])
        else:
            return ""
