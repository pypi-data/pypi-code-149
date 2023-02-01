from abc import ABCMeta, abstractmethod

from moocxing.package.MOOCXING import MODULE


class AbstractPlugin(metaclass=ABCMeta):
    def __init__(self):
        self.nlp = MODULE.nlp
        self.mqtt = MODULE.mqtt
        self.media = MODULE.media
        self.speech = MODULE.speech
        self.pinyin = MODULE.pinyin
        self.serial = MODULE.serial
        self.minecraft = MODULE.minecraft

    def say(self, text):
        self.speech.TTS(text)
        self.media.play()

    def play(self, path):
        self.media.play(path)

    def sayThread(self, text):
        self.speech.TTS(text)
        self.media.playThread()

    def playThread(self, path):
        self.media.playThread(path)

    @abstractmethod
    def isValid(self, query):
        return False

    @abstractmethod
    def handle(self, query):
        return None
