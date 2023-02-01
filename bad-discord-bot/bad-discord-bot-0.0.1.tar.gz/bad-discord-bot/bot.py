"""
MIT License

Copyright (c) 2023-present BattleTonk

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from .gateway_protocol import Gateway
from .api import DiscordAPI
from .embed import Embed
from .message import *


class Bot:
    def __init__(self, token, self_bot=False):
        if not self_bot:
            token = "Bot " + token
        self.discordApi = DiscordAPI(token)
        self._g = Gateway(token, self.discordApi)

    def run_gateway(self):
        self._g.run()

    def event(self, f):
        self._g.event(f)

    async def get_channel(self, channel_id):
        return await self.discordApi.get_channel(channel_id)

    async def respond_to_interaction(self, interaction_id, interaction_token):
        await self.discordApi.respond_to_interaction(interaction_id, interaction_token, "")


if __name__ == "__main__":
    past_invites = {}


    check_embed = False

    with open(".token") as token_file:
        token = token_file.read()
    bot = Bot(token)


    @bot.event
    async def message_reaction_add(msg):
        print("reaction added")

    @bot.event
    async def ready(msg):
        global past_invites
        past_invites = {}
        for invite in (await bot.discordApi.get_guild_invites(997981345403895878)):
            if invite["inviter"]["id"] in past_invites:
                past_invites[invite["inviter"]["id"]] += invite["uses"]
            else:
                past_invites[invite["inviter"]["id"]] = invite["uses"]
        print("ready")

    @bot.event
    async def message_create(msg):
        if msg.author.username == "ПАРОВОЗИК ТОМАС" and check_embed:
            embeds = []
            fields = [
                {
                    "name": "Я ЕБАЛ ГЕЙТВЕЙ ДИСКОРДА",
                    "value": "ПИСЬКОГРЫЗ ЧАТ БОТ УДАР\nПИСЬКОГРЫЗ ЧАТ БОТ УДАР",
                    "inline": True
                },
                {
                    "name": "Я ЕБАЛ ГЕЙТВЕЙ ДИСКОРДА2",
                    "value": "ПИСЬКОГРЫЗ ЧАТ БОТ УДАР\nПИСЬКОГРЫЗ ЧАТ БОТ УДАР",
                    "inline": True
                }
            ]
            thumbnail = {
                "url": "attachment://lel.png"
            }
            embed = Embed(title="Я ЕБАЛ ГЕЙТВЕЙ ДИСКОРДА", color=0x0000ff, fields=fields, thumbnail=thumbnail)
            embeds.append(embed)
            files = ["lel.png"]
            await msg.reply(embeds=embeds, files=files)

    @bot.event
    async def guild_member_add(msg):
        global past_invites
        current_invites = {}
        for invite in (await bot.discordApi.get_guild_invites(997981345403895878)):
            if invite["inviter"]["id"] in current_invites:
                current_invites[invite["inviter"]["id"]] += invite["uses"]
            else:
                current_invites[invite["inviter"]["id"]] = invite["uses"]
        for key in current_invites.keys():
            if key in past_invites:
                if past_invites[key] < current_invites[key]:
                    break
        past_invites = current_invites

    @bot.event
    async def guild_member_remove(msg):
        global past_invites
        current_invites = {}
        for invite in (await bot.discordApi.get_guild_invites(997981345403895878)):
            if invite["inviter"]["id"] in current_invites:
                current_invites[invite["inviter"]["id"]] += invite["uses"]
            else:
                current_invites[invite["inviter"]["id"]] = invite["uses"]
        for key in current_invites.keys():
            if key in past_invites:
                if past_invites[key] > current_invites[key]:
                    break
        past_invites = current_invites

    @bot.event
    async def interaction_create(msg):
        await bot.respond_to_interaction(msg["id"], msg["token"])


    bot.run_gateway()