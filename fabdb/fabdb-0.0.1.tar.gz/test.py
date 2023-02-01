from configparser import ConfigParser
import os

from fabdb.client import FabDBClient


config = ConfigParser()
config.read(os.path.expanduser("~/.config/fabdb"))

client = FabDBClient(config["DEFAULT"]["api_key"], config["DEFAULT"]["secret_key"])
res = client.get_deck("JReVoRdW")

print(res)
print(res.visibility)
for c in res.cards:
    print(c)
