from cerbeyra.src.dto.commons.va_item import VAItem
from cerbeyra.src.dto.cerbeyra_index import CerbeyraIndex
from cerbeyra.src.dto.probe import Probe
from cerbeyra.src.dto.sensor import Sensor
from cerbeyra.src.dto.client import Client


class CerbeyraIndexFactory:
    """
    Defines a factory method for building CerbeyraIndex objects.
    """

    @classmethod
    def build_from_json(cls, json_file: dict) -> CerbeyraIndex:
        """
        Builds a CerbeyraIndex object from the corresponding json data
        .
        :param json_file: a dictionary containing the CerbeyraIndex data.
        :return: a CerbeyraIndex object.
        """
        json_file['index'] = json_file.pop('cerbeyraIndex')
        return CerbeyraIndex(**json_file)


class ClientFactory:
    """
     Defines a factory method for building Client objects.
     """

    @classmethod
    def build_from_json(cls, json_file: dict) -> Client:
        """
        Builds a Client object from the corresponding json data.

        :param json_file: a dictionary containing Client data.
        :return: a Client object.
        """
        json_file['client_id'] = json_file.pop('id')
        return Client(**json_file)


class ProbeFactory:
    """
    Defines a factory method for building Probe objects.
    """

    @classmethod
    def build_from_json(cls, json_file: dict) -> Probe:
        """
        Builds a Probe object from the corresponding json data.

        :param json_file: a dictionary containing Probe data.
        :return: a Probe object.
        """
        json_file['last_update'] = json_file.pop('lastUpdate')
        json_file['probe_id'] = json_file.pop('id')
        client_json = json_file['client']
        json_file.pop('client')
        return Probe(**json_file, client=ClientFactory.build_from_json(client_json))


class SensorFactory:
    """
    Defines a factory method for building Sensor objects.
    """

    @classmethod
    def build_from_json(cls, json_file: dict) -> Sensor:
        """
        Builds a Sensor object from the corresponding json data.
        :param json_file: a dictionary containing Sensor data.
        :return: a Sensor object.
        """
        json_file['probe_gateway'] = json_file.pop('probeGateway')
        json_file['last_update'] = json_file.pop('lastUpdate')
        client_json = json_file['client']
        json_file.pop('client')
        return Sensor(**json_file, client=ClientFactory.build_from_json(client_json))


class VaItemFactory:
    """
    Defines a factory method for building VaItem objects.
    """

    @classmethod
    def build_from_row(cls, columns: list, entry_data: list) -> VAItem:
        """
        Builds a ReportItem object from key-value pairs specified in columns and
        entry_data respectively.

        :param columns: a list of fields either defined in WebReport or NetworkReport.
        :param entry_data: a list of values whose items are associated to the queried columns.
        :return: a ReportItem object.
        """
        d = {col: entry_data[i] for i, col in enumerate(columns)}
        return VAItem(**d)
