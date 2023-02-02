import json
import os

import telebot
from matplotlib import pyplot as plt
from telebot import apihelper
from telebot.types import InputMediaPhoto


class CreateAllure:

    def data_alure_report_artifacts(self):
        file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "allure-report/widgets/summary.json")
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return json.dumps(data, sort_keys=False, indent=4, ensure_ascii=False)

    def config_file(self):
        file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "notifications/config.json")
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return json.dumps(data, sort_keys=False, indent=4, ensure_ascii=False)

    def data_statistic(self):
        return json.loads(self.data_alure_report_artifacts())["statistic"]

    def data_config(self):
        return json.loads(self.config_file())["base"]

    def create_data(self):
        self.failed = self.data_statistic()['failed']
        self.broken = self.data_statistic()['broken']
        self.passed = self.data_statistic()['passed']
        self.skipped = self.data_statistic()['skipped']
        self.total = self.data_statistic()['total']
        self.name = self.data_config()['project']
        self.proxy = self.data_config()['proxy']
        self.token = self.data_config()['token']
        self.chat = self.data_config()['chat']
        self.reportLink = self.data_config()['reportLink']
        self.environment = self.data_config()['environment']
        labels = ['Успешные', 'Упавшие', 'Сломанные', 'Пропущенные']
        values = [self.passed, self.failed, self.broken, self.skipped]
        colors = ['#228B22', '#FF0000', '#FFD700', '#C0C0C0']
        explode = [0.0, 0.1, 0.0, 0.0]
        plt.title(f'{self.name}\n', fontdict={'fontweight': 600, 'fontsize': 'xx-large'})
        plt.pie(values, colors=colors, explode=explode, shadow=True, autopct='%1.1f%%', startangle=180)
        plt.axis('equal')
        plt.legend(labels=labels)
        return plt.savefig('allure_bot/allure.png')

    def send_messege(self):
        try:
            self.create_data()
            bot = telebot.TeleBot(f'{self.token}')
            bot.send_media_group(f'{self.chat}', [InputMediaPhoto(open('allure_bot/allure.png', 'rb'),
                                                                  parse_mode='HTML',
                                                                  caption=f'<b>Рабочее окружение:</b> {self.environment}'
                                                                          f'\n'
                                                                          f'\n<b>Всего тестов:</b> {self.total}'
                                                                          f'\n<b>Успешных тестов:</b> {self.passed}'
                                                                          f'\n<b>Упавших тестов:</b> {self.failed}'
                                                                          f'\n<b>Неисправных тестов:</b> {self.broken}'
                                                                          f'\n<b>Пропущенных тестов:</b> {self.skipped}'
                                                                          f'\n'
                                                                          f'\n<b>Отчет:</b> {self.reportLink}')])
        except:
            self.create_data()
            apihelper.proxy = {'https': f'{self.proxy}'}
            bot = telebot.TeleBot(f'{self.token}')
            bot.send_media_group(f'{self.chat}', [InputMediaPhoto(open('allure_bot/allure.png', 'rb'),
                                                                  parse_mode='HTML',
                                                                  caption=f'<b>Рабочее окружение:</b> {self.environment}'
                                                                          f'\n'
                                                                          f'\n<b>Всего тестов:</b> {self.total}'
                                                                          f'\n<b>Успешных тестов:</b> {self.passed}'
                                                                          f'\n<b>Упавших тестов:</b> {self.failed}'
                                                                          f'\n<b>Неисправных тестов:</b> {self.broken}'
                                                                          f'\n<b>Пропущенных тестов:</b> {self.skipped}'
                                                                          f'\n'
                                                                          f'\n<b>Отчет:</b> {self.reportLink}')])
