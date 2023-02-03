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


import requests
import json


COMPONENT_TYPES = {
    "Action Row"
}


class Component:
    def __init__(self):
        pass

    def get_data(self)->dict:
        return {}


class ActionRow(Component):
    def __init__(self, components=[]):
        super().__init__()
        self.components = components

    def get_data(self)->dict:
        data = {
            "type": 1,
            "components": [component.get_data() for component in self.components]
        }
        return data

    def add_component(self, component):
        self.components.append(component)


class Button(Component):
    def __init__(self, style=None, label=None, emoji=None, custom_id=None, url=None, disabled=False):
        super().__init__()
        self.style = style
        self.label = label
        self.emoji = emoji
        self.custom_id = custom_id
        self.url = url
        self.disabled = disabled

    def get_data(self)->dict:
        data = {
            "type": 2,
            "style": self.style,
            "label": self.label,
            "disabled": self.disabled
        }
        if self.style == 5:
            data["url"] = self.url
        else:
            data["custom_id"] = self.custom_id
            if self.emoji != None:
                pass
        return data


class Channel:
    def __init__(self, token:str, id:int, session:requests.Session):
        self.token = token
        self.id = id
        self.session = session

    def send_message(self, content=None, files=None, components=None):
        headers = {
            "authorization": self.token,
            "Content-type": "application/json"
        }

        body = {
        }
        if content != None:
            body["content"] = content

        if components != None:
            body["components"] = [component.get_data() for component in components]

        self.session.post(f"https://discord.com/api/v9/channels/{self.id}/messages", headers=headers, data=json.dumps(body))


class Client:
    def __init__(self, token:str, bot=True):
        self.token = "Bot " + token if bot else token
        self.session = requests.Session()

    def get_channel(self, id:int)->Channel:
        return Channel(self.token, id, self.session)

