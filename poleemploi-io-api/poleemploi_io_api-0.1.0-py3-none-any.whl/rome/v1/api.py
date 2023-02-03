
# https://pole-emploi.io/data/api/rome?tabgroup-api=documentation&doc-section=api-doc-section-caracteristiques
from ...base import Api as BaseApi
from typing import List
import requests


class Api(BaseApi):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        # params
        self.url = kwargs.get(
            "url", "https://api.pole-emploi.io/partenaire/rome/v1/")

    def scope(self) -> str:
        return "api_romev1 nomenclatureRome"

    def appellation(self, codes: List[str] = [], code: str = None, **kwargs):
        """
            codes: list of codes to search
            OR
            code: specific code to search

            **kwargs the rest of standard api calls (q, op, qf)
        """

        url = self.url + "/appellation"

        # get auth header
        headers = kwargs.pop("headers", {})
        headers = self._get_auth_header(headers)

        # priority given to search by code
        if code:
            url += f"/{code}"
            return requests.get(url, headers=headers)

        # codes search

        # transform into params
        params = [(k, kwargs[k])
                  for k in kwargs.keys()]

        # add the codes
        for code in codes:
            params.append(('code', code))

        return requests.get(url, params=params, headers=headers)

    def metier(self, **kwargs):
        url = self.url + "/metier"

        # get auth header
        headers = kwargs.pop("headers", {})
        headers = self._get_auth_header(headers)

        return requests.get(url, params=kwargs, headers=headers)

    def domaineprofessionnel(self, **kwargs):
        url = self.url + "/domaineprofessionnel"

        # get auth header
        headers = kwargs.pop("headers", {})
        headers = self._get_auth_header(headers)

        # params
        return requests.get(url, params=kwargs, headers=headers)
