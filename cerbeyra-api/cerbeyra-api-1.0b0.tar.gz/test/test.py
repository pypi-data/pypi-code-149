import os
import concurrent.futures
from src import CerbeyraClient
from src.constants.constants import NetworkReportFields


def req_info(cerbeyraclient: CerbeyraClient, clientid: int, columns: list) -> dict:
    res = {
        'cerbeyra_index': cerbeyraclient.get_cerbeyra_index(clientid),
        'report_network': cerbeyraclient.get_report_network(client_id=clientid, columns=columns),
        'report_web': cerbeyraclient.get_report_web(client_id=clientid),
    }
    return res


username_ = os.getenv('CERBEYRA_EMAIL')
password_ = os.getenv('CERBEYRA_PASSWORD')
endpoint = 'https://pre-areaclienti.cerbeyra.com'
res_path = '/'
params = [NetworkReportFields.host.value, NetworkReportFields.threat.value, NetworkReportFields.description.value]

with CerbeyraClient(username_, password_, endpoint) as cerbeyra_client:
    clients = cerbeyra_client.get_all_clients()
    clients = [client for client in clients if client.active]  # remove inactive clients
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_info = {
            executor.submit(req_info, cerbeyra_client, client.client_id, params): client.client_id for client in clients
        }
        for future in concurrent.futures.as_completed(future_to_info):
            client_id = future_to_info[future]
            data = future.result()
            report_network = data['report_network']
            grouped_repo = report_network.group_by_threat()
            if 'high' in grouped_repo.keys():
                host_list = [item.host for item in grouped_repo['high']]
                print(set(host_list))
            report_network.save_xls(f'{res_path}report_network_{client_id}.xlsx')
    print('Data saved')
