#!/usr/bin/env python3


import subprocess
import os
from plyer import notification

y = subprocess.getoutput("iwconfig wlan0")


def notif(mes):
    notification.notify(title="Done",
                        message=mes,
                        timeout=0)


if "Mode:Managed" in y:
    os.system("service NetworkManager stop ")
    os.system("ifconfig wlan0 down")
    os.system("iwconfig wlan0 mode monitor")
    os.system("ifconfig wlan0 up")
    notif("Monitor mode is enabled ")


if "Mode:Monitor" in y:
    os.system("ifconfig wlan0 down")
    os.system("iwconfig wlan0 mode managed")
    os.system("ifconfig wlan0 up")
    os.system("service NetworkManager start")
    notif("Monitor mode is disabled ")
