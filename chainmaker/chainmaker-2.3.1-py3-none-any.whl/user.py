import warnings

from chainmaker.client_user import ClientUser


class User(ClientUser):
    warnings.warn('请使用chainmaker.client_user.ClientUser', DeprecationWarning)
