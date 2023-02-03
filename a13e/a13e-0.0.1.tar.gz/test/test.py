import json
import os
import subprocess
import unittest
from pathlib import Path

import eyed3
import eyed3.id3

import a13e
from a13e.plugin import PluginRegister


class TestTag(unittest.TestCase):
    def setUp(self) -> None:
        self.song_tag_data = {
            "title": "千千阕歌",
            "artist": ["陈慧娴"],
            "album": "千千阕歌",
        }
        self.notag_mp3_fp = Path('test_notag.mp3')

    def test_tag(self):
        a13e.set_tag(self.notag_mp3_fp, self.song_tag_data)
        tag = eyed3.load(self.notag_mp3_fp).tag
        tag_dict = {'title': tag.title,
                    'album': tag.album,
                    'artist': tag.artist.split('/')}
        self.assertEqual(tag_dict, self.song_tag_data)

    def tearDown(self):
        mp3file = eyed3.load(self.notag_mp3_fp)
        mp3file.initTag()
        mp3file.tag.save(version=eyed3.id3.ID3_V2_3, encoding='utf-8')


class TestPlugin(unittest.TestCase):
    def test_load_plugin(self):
        import test_plugin
        PluginRegister(test_plugin)
        self.assertTrue(PluginRegister.recognizers.get('test_plugin1'))
        self.assertTrue(PluginRegister.recognizers.get('test_plugin2'))
        self.assertTrue(PluginRegister.recognizers.get('NeteaseCloudMusic'))

    def tearDown(self) -> None:
        PluginRegister.recognizers.pop('test_plugin1')
        PluginRegister.recognizers.pop('test_plugin2')


class TestRecognizer(unittest.TestCase):
    def setUp(self) -> None:
        self.mp3_fp = Path('test.mp3')

    def test_all_recognizer(self):
        for recognizer in PluginRegister.recognizers.values():
            self.assertTrue(recognizer.recognize(self.mp3_fp))


class TestCommand(unittest.TestCase):
    mp3_fp = Path('test.mp3').resolve()

    @classmethod
    def setUpClass(cls) -> None:
        os.chdir('../')
        cls.command = ['a13e', str(cls.mp3_fp)]

    def test_suppress(self):
        output = subprocess.check_output(self.command + ['-s'])
        self.assertFalse(output)

    def test_output(self):
        output = subprocess.check_output(self.command + ['-o', 'output.json'], encoding='gbk')
        output = list(eval(output))
        of = Path('output.json')
        self.assertEqual(json.loads(of.read_text('utf-8')), output)
        of.unlink(missing_ok=True)

    @classmethod
    def tearDownClass(cls) -> None:
        os.chdir('test')


if __name__ == '__main__':
    unittest.main()
