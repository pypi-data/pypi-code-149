import warnings

from chainmaker.client_node import ClientNode


class Node(ClientNode):
    warnings.warn('请使用chainmaker.client_node.ClientNode', DeprecationWarning)
