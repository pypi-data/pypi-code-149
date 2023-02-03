from typing import Dict, Union


class BaseSsdb:

    def auth(self, password: str) -> bool:
        pass

    def info(self) -> Dict[str, str]:
        pass

    def dbsize(self) -> int:
        pass

    def execute_command(self, cmd: str, *args) -> Union[None, list, int, bool]:
        pass
