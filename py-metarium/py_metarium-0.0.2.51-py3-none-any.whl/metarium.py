from .utils import (
    Serializer,
    LABEL_SUBSTRATE
)

class Metarium(Serializer, object):

    def __init__(self, **kwargs) -> None:
        self._reset()
        if "chain" in kwargs:
            assert "type" in kwargs["chain"]
            assert "parameters" in kwargs["chain"]
            if kwargs["chain"]["type"] == LABEL_SUBSTRATE:
                try:
                    from .chains import SubstrateChain
                    self.chain = SubstrateChain(**kwargs["chain"]["parameters"])
                    print(f"""         connected to {self.chain.info()["_SubstrateInterface__chain"]}!        """)
                except ImportError:
                    print("""         ERROR IMPORTING METARIUM SUBSTRATE CHAIN!     """)
                
    def _reset(self):
        self.chain = None

    def info(self):
        return {
            "chain" : self._recursive_serialize(self.chain.info()) if self.chain else None
        }
