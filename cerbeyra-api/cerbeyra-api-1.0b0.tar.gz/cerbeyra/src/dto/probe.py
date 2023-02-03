from dataclasses import dataclass
from cerbeyra.src.dto.client import Client
from cerbeyra.src.types import IoTStatus


@dataclass
class Probe:
    name: str
    probe_id: str
    status: IoTStatus
    last_update: str
    client: Client

    def __post_init__(self):
        if self.status is not None:
            self.status = IoTStatus(self.status)

    def __str__(self):
        """
        Defines the string representation for a probe object containing its probe_id and status.

        :return: the string representation.
        """
        return f'[{self.probe_id}] {self.name}: {self.status.value} - Client: {self.client}'
