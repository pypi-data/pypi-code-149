from abc import ABC, abstractmethod


class ITokenRepository(ABC):

    @abstractmethod
    def get_by_username(self, username):
        raise NotImplementedError()
