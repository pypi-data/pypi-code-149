import os
import re
from enum import Enum
import requests

from littlefieldpy.model.CompletedJobs import CompletedJobs
from littlefieldpy.model.Materials import Materials
from littlefieldpy.model.Orders import Orders
from littlefieldpy.model.Station import Station
from littlefieldpy.model.Paths import Paths

session_id_regex = re.compile(r'''JSESSIONID=(\w+);''')
points_regex = re.compile(r"""points: '((?:\d+ [\d.]+ ?)+)'""")
multi_points_regex = re.compile(r"""label: '([\d\w\s]+)', name: '([^']+)', points: '((?:\d+ [\d.]+ ?)+)'""")


class Littlefield:
    def __init__(self, institution, team_id='', password='', base_url='https://op.responsive.net/Littlefield/'):
        self.session_id = None
        if team_id == '' or password == '':
            self.team_id, self.password, self.institution = Littlefield._get_credentials_from_environment()
        else:
            self.team_id = team_id
            self.password = password
            self.institution = institution

        if self.team_id == '' or self.password == '' or self.institution == '':
            raise ValueError('TeamID, Password, and Institution are required!')

        # Ensure URL ends with /
        self.base_url = base_url.rstrip('/') + '/'

        self.update_session_id()

        self.orders = Orders(self)
        self.materials = Materials(self)
        self.station1 = Station(self, 1)
        self.station2 = Station(self, 2)
        self.station3 = Station(self, 3)
        self.completed_jobs = CompletedJobs(self)

    def cash(self, x='all'):
        return self.get_data(Paths.CASH, x)

    @staticmethod
    def _get_credentials_from_environment():
        tid = os.getenv('LITTLEFIELD_TEAM_ID', '')
        pw = os.getenv('LITTLEFIELD_PASSWORD', '')
        institution = os.getenv('LITTLEFIELD_INSTITUTION', '')
        return tid, pw, institution

    def update_session_id(self):
        self.session_id = self._get_session_id()

    def _get_session_id(self):
        headers = {'User-Agent': ''}
        payload = {'institution': self.institution, 'ismobile': 'false', 'id': self.team_id, 'password': self.password}
        r = requests.post(self.base_url + Paths.LOGIN.value, headers=headers, data=payload)
        cookie = r.headers.get('Set-Cookie')
        m = session_id_regex.search(cookie)
        if m is None:
            raise RuntimeError(r.text)

        return m.group(1)

    def get(self, path, params=None):
        cookie = {'JSESSIONID': self.session_id}
        r = requests.get(self.base_url + path, cookies=cookie, params=params)
        return r.text

    def set(self, path, data):
        cookie = {'JSESSIONID': self.session_id}
        r = requests.post(self.base_url + path, cookies=cookie, data=data)
        return r.text

    def get_data_multi(self, data, x='all'):
        if isinstance(data, Enum):
            data = data.value

        raw = self.get('Plot?data={}&x={}'.format(data, x))
        matches = multi_points_regex.findall(raw)
        if matches is None:
            self.update_session_id()
            raw = self.get('Plot?data={}&x={}'.format(data, x))
            matches = multi_points_regex.findall(raw)
            if matches is None:
                raise RuntimeError('failed to extract data')

        data = [(lbl, name, list(self._to_points(pts))) for lbl, name, pts in matches]
        return data

    def get_data(self, data, x='all'):
        if isinstance(data, Enum):
            data = data.value

        raw = self.get('Plot?data={}&x={}'.format(data, x))
        m = points_regex.search(raw)
        if m is None:
            self.update_session_id()
            raw = self.get('Plot?data={}&x={}'.format(data, x))
            m = points_regex.search(raw)
            if m is None:
                raise RuntimeError('failed to extract data')

        data = m.group(1)
        return list(self._to_points(data))

    @staticmethod
    def _to_points(data):
        points = [float(x) for x in data.split(' ')]
        for i in range(0, len(points), 2):
            yield points[i], points[i + 1]
