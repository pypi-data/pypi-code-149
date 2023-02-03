from dataclasses import dataclass
from cerbeyra.src.dto.client import Client
from cerbeyra.src.types import IoTStatus


@dataclass
class Sensor:
    name: str
    probe_gateway: str
    status: IoTStatus
    alarm: str
    last_update: str
    client: Client
    thresholds: list = None

    def __post_init__(self):
        if self.status is not None:
            self.status = IoTStatus(self.status)

    def __str__(self):
        """
        Defines the string representation for a sensor object containing its name and status.

        :return: the string representation.
        """
        return f'[{self.name}] {self.name}: {self.status.value} - Client: {self.client}'
