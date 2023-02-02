#
# MIT License
#
# Copyright (c) 2023 Wilhelm Ågren
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# File created: 2023-01-23
# Last updated: 2023-02-02
#

import requests
from gromp.api import BaseLeagueAPI
from gromp.utils import LeaguePLATFORMS, LeagueREGIONS

__all__ = (
    'AccountAPIv1',
)

class urls:
    puuid = '{region}.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}'
    gameNameTagLine = '{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}'
    me = '{region}.api.riotgames.com/riot/account/v1/accounts/me'
    gamePuuid = '{region}.api.riotgames.com/riot/account/v1/active-shards/by-game/{game}/by-puuid/{puuid}'

class AccountAPIv1(BaseLeagueAPI):
    """
    Official documentation:
    https://developer.riotgames.com/apis#account-v1
    """
    def __init__(self, platform=LeaguePLATFORMS.euw1, region=LeagueREGIONS.europe) -> None:
        super().__init__(self.__class__.__name__, platform, region)
    
    def puuid(self, token, puuid) -> requests.Response:
        """
        Get account by puuid.
        """
        self.set_params(region=self.region, puuid=puuid)
        http_response = self.get(
            token,
            urls.puuid,
        )

        return http_response
    
    def gameNameTagLine(self, token, gameName, tagLine) -> requests.Response:
        """
        Get account by riot id.
        """
        self.set_params(region=self.region, gameName=gameName, tagLine=tagLine)
        http_response = self.get(
            token,
            urls.gameNameTagLine,
        )

        return http_response
    
    def me(self, token) -> requests.Response:
        """
        Get account by access token.
        """
        self.set_params(region=self.region)
        http_response = self.get(
            token,
            urls.me,
        )

        return http_response

    def gamePuuid(self, token, game, puuid) -> requests.Response:
        """
        Get active shard for a player.
        """
        self.set_params(region=self.region, game=game, puuid=puuid)
        http_response = self.get(
            token,
            urls.gamePuuid,
        )

        return http_response
