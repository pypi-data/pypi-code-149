import requests
import os
import random
import ffmpeg

from moocxing.robot import Constants
from moocxing.plugins.sdk.AbstractPlugin import AbstractPlugin
from moocxing.robot import Config
from moocxing.robot.utils import yamlUtils


class Plugin(AbstractPlugin):
    SLUG = "music"

    def getMusicInfo(self, keyword):
        # 如果没识别到关键词，从排行榜获取
        if keyword == "":
            url = f"{Config.get('netease/baseUrl')}/personalized/newsong"
            self.music_info = requests.get(url).json()["result"][random.randint(0, 9)]["song"]
        else:
            url = f"{Config.get('netease/baseUrl')}/search?keywords={keyword}"
            self.music_info = requests.get(url).json()["result"]["songs"][0]
        # 获取歌曲id
        self.music_id = self.music_info["id"]
        # 获取歌曲名字
        self.music_name = self.music_info["name"].replace(" ","_")
        # 获取歌手名称
        self.music_singer = ""
        for artists in self.music_info["artists"]:
            self.music_singer = self.music_singer + artists["name"] + '、'
        self.music_singer = self.music_singer[:-1].replace(" ","_")

    def getMusicUrl(self):
        url = f"https://music.163.com/song/media/outer/url?id={self.music_id}.mp3"
        self.music_url = requests.get(url).url


    def downMusic(self, keyword):
        # 获取歌曲信息
        self.getMusicInfo(keyword)
        # 获取歌曲URL
        self.getMusicUrl()

        # 指定用户路径
        dir_path = Constants.PATH_CUSTOM_MUSIC
        # 在用户路径 创建文件夹
        yamlUtils.mkdir(dir_path)
        # 拼接文件名称
        path = os.path.join(dir_path, f"{self.music_name}-{self.music_singer}.mp3")
        self.out_path = path.replace('mp3', 'wav')
        # 下载文件
        os.system(f"curl -so {path} {self.music_url}")
        # 文件转码 mp3 => wav
        ffmpeg.run(ffmpeg.output(
            ffmpeg.input(path), self.out_path),
            quiet=True,
            overwrite_output=True
        )

    def handle(self, query):
        # 获取歌曲关键词
        keyword = self.nlp.getMusicName(query)
        self.say(f"正在为你准备{keyword}")
        self.downMusic(keyword)
        self.playThread(self.out_path)
    
    def isValid(self, query):
        return any(word in query for word in ["听", "播放", "首", "歌"])
