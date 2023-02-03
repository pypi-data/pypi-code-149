import re
from collections import namedtuple

from littlefieldpy.model.Paths import Paths

MaterialsInfo = namedtuple('MaterialsInfo',
                           ['unit_cost', 'order_cost', 'lead_time', 'reorder_point', 'order_quantity',
                            'next_arrival_quantity', 'next_arrival_eta'])

materials_info_regex = re.compile(r'''<BR><B>Unit Cost: </B> \$ ([\d.]+)
<BR><B>Order Cost: </B> \$ ([\d.]+)
<BR><B>Lead Time:</B> (\d+) day\(s\)
<BR><B>Reorder Point:</B> ([\d,]+) kits
<BR><B>Order Quantity:</B>
([\d,]+) kits
(?:<P><B>Material order of ([\d,]+)\s+kits due to arrive in ([\d.]+) simulated days)?''')


def parse_materials_info(unit_cost, order_cost, lead_time, reorder_point,
                         order_quantity, next_arrival_quantity=None, next_arrival_eta=None):
    unit_cost = float(unit_cost)
    order_cost = float(order_cost)
    lead_time = int(lead_time)
    reorder_point = int(reorder_point.replace(',', ''))
    order_quantity = int(order_quantity.replace(',', ''))
    if next_arrival_quantity is not None:
        next_arrival_quantity = int(next_arrival_quantity.replace(',', ''))
    if next_arrival_eta is not None:
        next_arrival_eta = float(next_arrival_eta)

    return MaterialsInfo(unit_cost, order_cost, lead_time, reorder_point,
                         order_quantity, next_arrival_quantity, next_arrival_eta)


class Materials:
    def __init__(self, lf):
        self.lf = lf

    def inventory(self, x='all'):
        return self.lf.get_data(Paths.INVENTORY, x)

    def info(self, update=False) -> MaterialsInfo:
        params = {update: 'update'} if update else None
        raw = self.lf.get('MaterialMenu', params)
        m = materials_info_regex.search(raw)
        if m is None:
            self.lf.update_session_login()
            raw = self.lf.get('MaterialMenu', params)
            m = materials_info_regex.search(raw)
            if m is None:
                raise RuntimeError('failed to get material info')

        return parse_materials_info(*m.groups())
