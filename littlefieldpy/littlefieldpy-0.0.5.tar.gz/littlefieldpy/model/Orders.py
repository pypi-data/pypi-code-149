import re
from collections import namedtuple

from littlefieldpy.model.Paths import Paths

OrdersInfo = namedtuple('OrdersInfo',
                        ['wip_limit', 'kits_per_job', 'lot_size', 'lots_per_job', 'current_contract',
                         'quoted_lead_time', 'max_lead_time', 'revenue_per_order'])

orders_info_regex = re.compile(r'''<b>Maximum WIP Limit: </b>(\d+) jobs<BR>
<B>Number of kits in 1 job: </B>(\d+)<BR>
<B>Lot size: </B>(\d+) kits, or (\d+) lots? per job<BR>
<B>Current contract: </B>(\d+)<BR>
<DD>Quoted lead time: ([\d.]+) day\(s\)<BR>
<DD>Maximum lead time: ([\d.]+) day\(s\)<BR>
<DD>Revenue per order: ([\d.]+) dollars<BR><HR>''')


def parse_orders_info(wip_limit, kits_per_job, lot_size, lots_per_job, current_contract, quoted_lead_time,
                      max_lead_time, revenue_per_order):
    wip_limit = int(wip_limit)
    kits_per_job = int(kits_per_job)
    lot_size = int(lot_size)
    lots_per_job = int(lots_per_job)
    current_contract = int(current_contract)
    quoted_lead_time = float(quoted_lead_time)
    max_lead_time = float(max_lead_time)
    revenue_per_order = float(revenue_per_order)
    return OrdersInfo(wip_limit, kits_per_job, lot_size, lots_per_job, current_contract, quoted_lead_time,
                      max_lead_time, revenue_per_order)


class Orders:
    def __init__(self, lf):
        self.lf = lf

    def job_arrivals(self, x='all'):
        return self.lf.get_data(Paths.JOBS_IN, x)

    def queued_jobs(self, x='all'):
        return self.lf.get_data(Paths.QUEUED_JOBS, x)

    def info(self, update=False) -> OrdersInfo:
        params = {update: 'update'} if update else None
        raw = self.lf.get('OrdersMenu', params)
        m = orders_info_regex.search(raw)
        if m is None:
            self.lf.update_session_login()
            raw = self.lf.get('OrdersMenu', params)
            m = orders_info_regex.search(raw)
            if m is None:
                raise RuntimeError('failed to get customer orders')

        return parse_orders_info(*m.groups())
