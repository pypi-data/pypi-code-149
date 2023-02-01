from setuptools import setup, find_packages

setup(
    name='command_telegram_allure_lib',
    version='1.1',
    packages=find_packages(),
    entry_points = {
      'console_scripts':
            [
                'create_notify_dir = command_telegram_allure_lib.Start:startapp',
                'get_allure_report = command_telegram_allure_lib.Start:messege'
             ]
    },
    author_email='gorelov2895@yandex.ru'
)
