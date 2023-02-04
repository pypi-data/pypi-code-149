import requests
import asyncio
import aiohttp

class Moon:
    flow_key = 'Gy5dlw8OEVzbFvW2xHYo/1'
    api_key = '602d9493-7a8f-4a50-ab3d-e8693f7c837f'

    def __init__(self, opening, closing, utctime):
        self.opening = opening
        self.closing = closing
        self.utctime = utctime

    
    def getUtcHour(self):
        return str(self.utctime).split(' ')[1][1]


    def prepData(self):
        avr = self.closing/(self.opening + self.closing)
        bvr = self.opening/(self.opening + self.closing)
        time = self.getUtcHour()

        data = {
            'avr': avr,
            'bvr': bvr,
            'time': time
        }

        return data

    async def getRes(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f'https://api.akk.io/api?flow_key={self.flow_key}&api_key={self.api_key}&data=%5B%7B%22avr%22%3A%22{self.prepData().get("avr")}%22%2C%22bvr%22%3A%22{self.prepData().get("bvr")}%22%2C%22time%22%3A%22{self.prepData().get("time")}%22%7D%5D'
            ) as response:
                response_json = await response.json()
                return response_json[0].get('class')

    async def main(self):
        res = await asyncio.gather(self.getRes())
        return res

def signal(
    opening: float,
    closing: float,
    utctime: str
    ):
    return int(asyncio.run(Moon(opening, closing, utctime).main())[0])