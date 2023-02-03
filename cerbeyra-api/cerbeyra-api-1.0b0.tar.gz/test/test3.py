import os
from cerbeyra import CerbeyraApi
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

username = os.getenv('CERBEYRA_EMAIL')
password = os.getenv('CERBEYRA_PASSWORD')

with CerbeyraApi(username, password, auto_reconnect=False) as cerbeyra_api:
    clients = cerbeyra_api.get_all_clients()
    for c in clients:
        print(c)
    ci = cerbeyra_api.get_cerbeyra_index(127)
    print(ci)
    probes = cerbeyra_api.get_all_probes(status='DANGER')
    for p in probes:
        print(p)
    sensors = cerbeyra_api.get_all_sensors()
    for s in sensors:
        print(s)
    exit(0)
    net_repo = cerbeyra_api.get_report_network(client_id=127, columns=['threat', 'host', 'vuln_id'])
    hosts = net_repo.get_distinct_hosts()
    print(hosts)
    web_repo = cerbeyra_api.get_report_web(client_id=127, columns=['threat', 'url', 'vuln_id'])
    grouped_web = web_repo.group_by_threat()
    if 'high' in grouped_web.keys():
        for item in grouped_web['high']:
            print(item.get_field('url'))

    sensors = cerbeyra_api.get_all_sensors()
    probes = cerbeyra_api.get_all_probes()

    for probe in probes:
        print(probe)

    for sensor in sensors:
        print(sensor)
