from py_metarium import (
    Metarium, LABEL_SUBSTRATE
)

METARIUM_EXTRINSIC = "Metarium"


class Decoder:

    def __init__(self, url=None) -> None:
        url = url or None
        assert url is not None
        initialization_parameters = {
            "chain": {
                "type": LABEL_SUBSTRATE,
                "parameters": {
                    "url" : url
                }
            }
        }

        m = Metarium(**initialization_parameters)

        self.metarium_node = m.chain
    
    def info(self):
        return self.metarium_node.info()

    def get_block_hash_from_block_number(self, block_number: int) -> str:
        return self.metarium_node.get_block_hash_from_block_number(block_number)
    
    def get_tip_number(self, finalized_only: bool=False) -> int:
        return self.metarium_node.get_tip_number(finalized_only=finalized_only)

    def __decode_blocks(self, direction:str, block_hash:str=None, block_count:int=None):
        return self.metarium_node.get_blocks(direction=direction, block_hash=block_hash, block_count=block_count)

    def decode(self, direction, block_hash=None, block_count=None):
        return self.__decode_blocks(direction, block_hash=block_hash, block_count=block_count)
    
    def decode_metarium(self, direction, block_hash=None, block_count=None):
        for block in self.__decode_blocks(direction, block_hash=block_hash, block_count=block_count):
            has_metarium_call = False
            for extrinsic in block["extrinsics"]:
                if extrinsic['call']['call_module']['name'] == METARIUM_EXTRINSIC:
                    has_metarium_call = True
            
            yield block, has_metarium_call
    
    def decode(self, direction, block_hash=None, block_count=None):
        return self.metarium_node.get_points(direction=direction, block_hash=block_hash, block_count=block_count)
