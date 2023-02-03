import math
import time

from substrateinterface import SubstrateInterface

from ..utils import FUTURE, PAST
from .base import Chain
from ..utils import ChainConnectionRefusedError

ALL_BLOCKS = math.inf


class SubstrateChain(Chain):

    def __init__(self, *args, **kwargs) -> None:
        reconnection_attempts = 1
        while True:
            try:
                self.__client = SubstrateInterface(
                    url=kwargs.get("url", "ws://127.0.0.1:9944")
                )
            except ConnectionRefusedError:
                if reconnection_attempts == self.__class__.MAX_RECONNECTION_ATTEMPTS:
                    print(f"Chain connection terminated after {reconnection_attempts} attempts.")
                    raise ChainConnectionRefusedError
                print(f"Chain connection refused. Retrying in {self.__class__.RECONNECTION_WAIT_DURATION_SECONDS} seconds ...")
                reconnection_attempts += 1
                time.sleep(self.__class__.RECONNECTION_WAIT_DURATION_SECONDS)
                continue
            break
        
        self._reset_cached_blocks()
        self._reset_block_headers()

    def prefix(self):
        return self.__class__.POINT_PREFIX
    
    def info(self):
        return self.__client.__dict__

    def _reset_cached_blocks(self):
        self.__cached_blocks = {}

    def _reset_block_headers(self):
        self.__current_block = None
        self.__current_block_header = {}
        self.__current_block_number = -1

    def _set_current_block(self, block_hash=None, block_number=None, persevere=False):
        current_block = self.__client.get_block(block_hash=block_hash or None, block_number=block_number or None)
        if persevere:
            while (current_block is None):
                current_block = self.__client.get_block(block_hash=block_hash or None, block_number=block_number or None)
        if current_block and current_block["header"]["number"] != self.__current_block_number:
            self.__current_block = current_block
            self.__current_block_header = self.__current_block["header"]
            self.__current_block_number = self.__current_block_header["number"]


    def get_blocks(self, direction, block_hash=None, block_count=None) -> None:
        """
            if direction is PAST:
                if block_hash is None:
                    if block_count is None:
                        _get_blocks(start=now, end=block_0, block_count="all")
                    else:
                        _get_blocks(start=now, end=block_0, block_count=block_count)
                else:
                    if block_count is None:
                        _get_blocks(start=block_({block_hash}), end=block_0, block_count="all")
                    else:
                        _get_blocks(start=block_({block_hash}), end=block_0, block_count=block_count)
            else:#if direction is FUTURE
                if block_hash is None:
                    if block_count is None:
                        _stream_blocks(start=now, block_count="all")
                    else:
                        _stream_blocks(start=now, block_count=block_count)
                else:
                    if block_count is None:
                        _stream_blocks(start=block_({block_hash}), block_count="all")
                    else:
                        _stream_blocks(start=block_({block_hash}), block_count=block_count)
        """
        # sanitize inputs
        assert direction in (FUTURE, PAST)
        # reset cache
        self._reset_cached_blocks()
        self._reset_block_headers()
        self._set_current_block(block_hash=block_hash)
        # set direction and block_count
        if block_count is None:
            if direction == PAST:
                block_count = self.__current_block_number
            else:
                block_count = ALL_BLOCKS
        # _get_blocks()
        while len(self.__cached_blocks) < block_count:
            if self.__current_block_number in self.__cached_blocks:
                continue
            # add block_number to cache
            self.__cached_blocks[self.__current_block_number] = self.__current_block
        
            # remove previous block_number from cache if we are getting points into the future
            if (block_count == ALL_BLOCKS) and \
                (str(self.__current_block_number -1) in self.__cached_blocks):
                del self.__cached_blocks[self.__current_block_number-1]
            
            yield self.__current_block
            
            if direction == PAST:
                self._set_current_block(block_number=self.__current_block_number-1, persevere=True)
            else:
                try:
                    self._set_current_block(block_number=self.__current_block_number+1, persevere=True)
                except TypeError:
                    pass
        
    def get_block_hash_from_block_number(self, block_number: int) -> str:
        return self.__client.get_block_hash(block_number)
    
    def get_tip_number(self, finalized_only: bool=False) -> int:
        finalized_only = finalized_only or False
        block = self.__client.get_block(finalized_only=finalized_only)
        return block["header"]["number"]
