from __future__ import absolute_import

__author__ = "Flavio Garcia <piraz@candango.org>"
__version__ = (0, 0, 0, 1)
__licence__ = "Apache License V2.0"


def get_version():
    if isinstance(__version__[-1], str):
        return '.'.join(map(str, __version__[:-1])) + __version__[-1]
    return ".".join(map(str, __version__))


def get_author():
    return __author__.split(" <")[0]


def get_author_email():
    return __author__.split(" <")[1][:-1]


try:
    import etcd3.etcdrpc as etcdrpc
    from etcd3.client import Endpoint
    from etcd3.client import Etcd3Client
    from etcd3.client import MultiEndpointEtcd3Client
    from etcd3.client import Transactions
    from etcd3.client import client
    from etcd3.exceptions import Etcd3Exception
    from etcd3.leases import Lease
    from etcd3.locks import Lock
    from etcd3.members import Member

    __all__ = (
        'etcdrpc',
        'Endpoint',
        'Etcd3Client',
        'Etcd3Exception',
        'Transactions',
        'client',
        'Lease',
        'Lock',
        'Member',
        'MultiEndpointEtcd3Client'
    )
# Will try to load modules not found during a clean installation.
# Ignoring this error here.
except ModuleNotFoundError:
    pass
