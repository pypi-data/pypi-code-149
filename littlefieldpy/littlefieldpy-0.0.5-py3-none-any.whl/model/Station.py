import re
from collections import namedtuple

station_info_regex = re.compile(r'''<P><B> Number of Machines: <\/B>(\d+)<BR>
<B>Scheduling Policy: </B>([\w\s]+)<BR>
<B>Purchase Price: </B>\$\s*([\d,]+\.\d{2})<BR>
<B>Retirement Price: </B>\$\s*([\d,]+\.\d{2})<BR>''')

StationInfo = namedtuple('StationInfo', ['num_machines', 'scheduling_policy', 'purchase_price', 'retirement_price'])


def parse_station_info(num_machines, scheduling_policy, purchase_price, retirement_price):
    num_machines = int(num_machines)
    purchase_price = float(purchase_price.replace(',', ''))
    retirement_price = float(retirement_price.replace(',', ''))

    return StationInfo(num_machines, scheduling_policy, purchase_price, retirement_price)


class Station:
    def __init__(self, lf, station_id):
        self.lf = lf
        self.station_id = station_id

    def queue_size(self, x='all'):
        return self.lf.get_data('S{}Q'.format(self.station_id), x)

    def utilization(self, x='all'):
        return self.lf.get_data('S{}UTIL'.format(self.station_id), x)

    def info(self, update=False) -> StationInfo:
        params = {update: 'update'} if update else None
        raw = self.lf.get('StationMenu?id={}'.format(self.station_id), params)
        m = station_info_regex.search(raw)
        if m is None:
            self.lf.update_session_login()
            raw = self.lf.get('StationMenu?id={}'.format(self.station_id), params)
            m = station_info_regex.search(raw)
            if m is None:
                raise RuntimeError('failed to get station info')

        return parse_station_info(*m.groups())
