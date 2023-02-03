from typing import List

from cerbeyra.src.cerbeyra_client import CerbeyraClient
from cerbeyra.src.dto import CerbeyraIndex, NetworkReport, WebReport, Client, Probe, Sensor
from cerbeyra.src.dto.factories.factories import CerbeyraIndexFactory, ClientFactory, ProbeFactory, SensorFactory
from cerbeyra.src.types import APIurls, PartnerAPIurls, network_default_columns, web_default_columns
from cerbeyra.utils import stream_response_to_temp_file


class BaseApi:
    """
    Encloses a set of functions to make it easier getting resources through the Cerbeyra's APIs.
    It wraps CerbeyraClient.
    """

    def __init__(self, username: str = None, password: str = None, endpoint: str = None, auto_reconnect=False):
        """
        Builds a CerbeyraClient object to be used for negotiating with Cerbeyra.

        :param username: the email for authentication.
        :param password: the password for authentication.
        :param endpoint: the endpoint exposing Cerbeyra's API.
        :param auto_reconnect: a boolean indicating whether auto reconnection is needed after token expiration.
        """
        self._client = CerbeyraClient(username=username, password=password,
                                      endpoint=endpoint, auto_reconnect=auto_reconnect)

    def __enter__(self):
        """
        Makes the client callable with a context manager.

        :return: an already connected CerbeyraClient object.
        """
        self._client.login()
        return self

    def __exit__(self, *args):

        pass

    def get_cerbeyra_index(self, client_id: int = None) -> CerbeyraIndex:
        """
        Returns the *Cerbeyra Index* of the logged user.
        *For Partners Only:* you can specify the client_id to obtain the *Cerbeyra Index* of a specific client.

        :param client_id: the unique identifier of a client.
        :return: a Cerbeyra Index object.
        """
        if not client_id:
            url = APIurls.cerbeyra_index.value
        else:
            url = PartnerAPIurls.cerbeyra_index.value.format(client_id=client_id)
        ci_response = self._client.get(url)
        return CerbeyraIndexFactory.build_from_json(ci_response.json())

    def get_report_network(self, columns: list[str] = None, client_id: int = None) -> NetworkReport:
        """
        Get the list of every vulnerability detected on your account on every network host.
        you can select a list of columns using the Enum class : types.NetworkReportFields,
        otherwise the API will return a default set of column.
        *For Partners Only:* you can specify a client_id to obtain the information about one of your client.


        :param columns: a list of report fields (defining the query string).
        :param client_id: the unique identifier of a specific client.
        :return: a NetworkReport object.
        """
        if not columns:
            columns = network_default_columns
        params = {'column[]': columns}

        if not client_id:
            url = APIurls.report_network.value
        else:
            url = PartnerAPIurls.report_network.value.format(client_id=client_id)

        csv_response = self._client.get(url, params=params, stream=True)
        csv_file = stream_response_to_temp_file(csv_response)
        return NetworkReport(csv_file, columns)

    def get_report_web(self, columns: list[str] = None, client_id: int = None) -> WebReport:
        """
        Get the list of every vulnerability detected on your account on every web host.
        you can select a list of columns using the Enum class : types.WebReportFields,
        otherwise the API will return a default set of column.
        *For Partners Only:* you can specify a client_id to obtain the information about one of your client.

        :param client_id: the unique identifier of a specific client.
        :param columns: a list of report fields (defining the query string).
        :return: a WebReport object.
        """
        if not columns:
            columns = web_default_columns
        params = {'column[]': columns}

        if not client_id:
            url = APIurls.report_web.value
        else:
            url = PartnerAPIurls.report_web.value.format(client_id=client_id)
        csv_response = self._client.get(url, params=params, stream=True)
        csv_file = stream_response_to_temp_file(csv_response)
        return WebReport(csv_file, columns)

    def get_all_clients(self) -> List[Client]:
        """
        *For Partners Only:* gets the list of all clients.

        :return: a list of Client objects.
        """
        url = PartnerAPIurls.clients_list.value
        clients_response = self._client.get(url)
        try:
            return [ClientFactory.build_from_json(client) for client in clients_response.json()['clients']]
        except KeyError:
            return []

    def get_all_probes(self, status: str = None) -> List[Probe]:
        """
        *For Partners Only:* gets the list of all probes.
        You can specify a status *(ALIVE, WARNING, DANGER)* to filter away the probes you are not interested on.

        :param status: a probe status (defining the query string).
        :return: a list of Probe objects.
        """
        params = {}
        if status:
            params = {'status': status}

        url = PartnerAPIurls.probes_list.value
        probes_response = self._client.get(url, params=params)
        return [ProbeFactory.build_from_json(probe) for probe in probes_response.json()]

    def get_all_sensors(self, status: str = None) -> List[Sensor]:
        """
        *For Partners Only:* gets the list of all IoT sensors.
        You can specify a status *(ALIVE, WARNING, DANGER)* to filter away the sensors you are not interested on.

        :param status: a sensor status (defining the query string).
        :return: a list of Sensor objects.
        """
        params = {}
        if status:
            params = {'status': status}
        url = PartnerAPIurls.sensor_list.value
        sensors_response = self._client.get(url, params=params)
        return [SensorFactory.build_from_json(sensor) for sensor in sensors_response.json()]
