from typing import List, Dict, Optional

from base_ssdb import BaseSsdb
from utils import SsdbResponseUtils


class BaseSsdbHash(BaseSsdb):

    def hincr(self, name: str, k: any, num: int) -> int:
        pass

    def hset(self, name: str, k: any, v: any):
        pass

    def hget(self, name: str, k: any) -> Optional[bytes]:
        pass

    def hsize(self, name: str) -> int:
        pass

    def hexists(self, name: str, k: any) -> bool:
        pass

    def hdel(self, name: str, k: any):
        pass

    def hclear(self, name: str):
        pass

    def multi_hset(self, name: str, data: Dict[any, any]):
        pass

    def multi_hget(self, name: str, keys: List[str]) -> Dict[bytes, bytes]:
        pass


class SsdbHash(BaseSsdbHash):

    def hincr(self, name: str, k: any, num: int) -> int:
        result = self.execute_command('hincr', name, k, num)
        return int(result)

    def hset(self, name: str, k: any, v: any):
        self.execute_command('hset', name, k, v)

    def hget(self, name: str, k: any) -> Optional[bytes]:
        return self.execute_command('hget', name, k)

    def hsize(self, name: str) -> int:
        return int(self.execute_command('hsize', name))

    def hexists(self, name: str, k: any) -> bool:
        result = self.execute_command('hexists', name, k)
        return True if int(result) == 1 else False

    def hdel(self, name: str, k: any):
        self.execute_command('hdel', name, k)

    def hclear(self, name: str):
        self.execute_command('hclear', name)

    def multi_hset(self, name: str, data: Dict[any, any]):
        pairs = SsdbResponseUtils.encode_dict_to_pairs(data)
        self.execute_command('multi_hset', name, *pairs)

    def multi_hget(self, name: str, keys: List[str]) -> Dict[bytes, bytes]:
        result = self.execute_command('multi_hget', name, *keys)

        return SsdbResponseUtils.response_to_map(result)
