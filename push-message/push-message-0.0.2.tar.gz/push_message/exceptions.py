class QYWXIdSecretInvalidError(Exception):
    def __init__(self, msg=None):
        self.msg = msg

    def __str__(self):
        if self.msg is not None:
            return self.msg
        return 'CORP_ID and CORP_SECRET for QYWX are invalid.'


class QYWXTokenInvalidError(Exception):
    def __init__(self, msg=None):
        self.msg = msg

    def __str__(self):
        if self.msg is not None:
            return self.msg
        return 'token for QYWX is invalid.'
