from django.conf import settings


class SmtpConf:
    def __init__(self):
        self.__smtp = settings.EMAIL_HOST,
        self.port = settings.EMAIL_PORT
        self.use_tls = settings.EMAIL_USE_TLS
        self.user = settings.EMAIL_HOST_USER
        self.password = settings.EMAIL_HOST_PASSWORD
        self.app_name = settings.APPLICATION_NAME

    @property
    def smtp(self):
        return self.__smtp[0] if self.__smtp is not None else None


class EmailHtml:
    def __init__(self, subject: str,
                 text_message: str,
                 html_message: str,
                 to: str,
                 sender_email: str = None,
                 sender_name: str = None,
                 sender_name_on_subject=False):
        self.subject = subject
        self.text_message = text_message
        self.html_message = html_message
        self.to = to
        self.sender_email = sender_email
        self.sender_name = sender_name
        self.sender_name_on_subject = sender_name_on_subject
