import os
import time

from src.constants.constants import NetworkReportFields
from src.exceptions.exceptions import APIException
from src import CerbeyraClient


endpoint = 'https://areaclienti.cerbeyra.com/'
username_ = os.getenv('CERBEYRA_EMAIL')
password_ = os.getenv('CERBEYRA_PASSWORD')
fields = [NetworkReportFields.host.value, NetworkReportFields.threat.value, NetworkReportFields.description.value]

# Test1 auto-reconnect (expire_time fixed to 60secs).
#
# with CerbeyraClient(username_, password_, endpoint) as cerbeyra_client:
#     for _ in range(4):
#         index = cerbeyra_client.get_cerbeyra_index()
#         print(index.cerbeyra_index)
#         time.sleep(30)


# Test2 get user's cerbeyra index
with CerbeyraClient(username_, password_, endpoint) as cerbeyra_client:
    try:
        index = cerbeyra_client.get_cerbeyra_index()
        print(f'User -> cerbeyra_index={index.index}')
    except APIException as err:
        print(err)

# Test3 get clients' cerbeyra index
with CerbeyraClient(username_, password_, endpoint) as cerbeyra_client:
    clients = cerbeyra_client.get_all_clients()
    # clients = [client for client in clients if client.active]
    for client in clients:
        try:
            index = cerbeyra_client.get_cerbeyra_index(client.client_id)
            print(f'{client} -> cerbeyra_index={index.index}')
        except APIException as err:
            print(f'{client} -> {err}')

# Test4 get clients' network report and scanned hosts list
with CerbeyraClient(username_, password_, endpoint) as cerbeyra_client:
    clients = cerbeyra_client.get_all_clients()
    for client in clients:
        try:
            report = cerbeyra_client.get_report_network(client_id=client.client_id, columns=fields)
            report.save_xls(f'report_network_{client.client_id}.xlsx')
            hosts = report.get_distinct_hosts()
            print(f'{client} -> {hosts}')
        except APIException as err:
            print(f'{client} -> {err}')

# Test5 get IoT info
with CerbeyraClient(username_, password_, endpoint) as cerbeyra_client:
    probes = cerbeyra_client.get_all_probes()
    sensors = cerbeyra_client.get_all_sensors()
    for probe in probes:
        print(probe)
