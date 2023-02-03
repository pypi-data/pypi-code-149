from dataclasses import dataclass


@dataclass
class Client:
    client_id: int
    name: str
    surname: str
    email: str
    company: str
    active: bool
    expiration_date: str = None

    def __str__(self):
        """
        A string representation of a Client object containing its client_id, name and surname.

        :return: the string representation.
        """
        return f'[{self.client_id}] {self.company} ({self.name} {self.surname})'
