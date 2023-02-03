class Chain(object):

    RECONNECTION_WAIT_DURATION_SECONDS = 5
    MAX_RECONNECTION_ATTEMPTS = 10
    POINT_PREFIX = "chain"

    # common functions for Encoders and Decoders
    def prefix(self):
        raise NotImplementedError
    
    def info(self):
        raise NotImplementedError
    
    # Decoder-specific functions
    def get_blocks(self):
        raise NotImplementedError
    
    def get_block_hash_from_block_number(self, block_number):
        raise NotImplementedError
    
    def get_tip_number(self, finalized_only=False):
        raise NotImplementedError
