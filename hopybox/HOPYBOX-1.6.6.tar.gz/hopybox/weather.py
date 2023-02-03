import requests as visit
from .translate import translate
from rich.console import Console

console = Console()

def city(city):
  with console.status("\033[96mLoaing weather …\033[0m"):
    print('\033[92m'+translate(visit.get('https://xiaobai.klizi.cn/API/other/qq_weather.php?&msg={}'.format(city)).text))