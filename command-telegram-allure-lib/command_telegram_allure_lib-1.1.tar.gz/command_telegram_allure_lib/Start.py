from python_telegram_allure_notify.AllureBot import CreateAllure

def messege():
    messege = CreateAllure()
    messege.send_messege()

import os

os.mkdir("notifications")


def dir_data():
    init = open("notifications/__init__.py", "w+")
    init.close()
    db_data = open("notifications/config.json", "w+")
    db_data.close()


def startapp():
    dir_data()
