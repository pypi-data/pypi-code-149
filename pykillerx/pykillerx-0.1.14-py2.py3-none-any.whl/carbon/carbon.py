from io import BytesIO
from aiohttp import ClientSession
from pyrogram import *
from pyrogram.types import *
import json
import os
import requests

async def make_carbon(code):
    aiosession = ClientSession()
    url = "https://carbonara.vercel.app/api/cook"
    async with aiosession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image
