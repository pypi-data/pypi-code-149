import logging

from .defines import CK
from .wsHandle import InoDriveWS
from .file import InoDriveFile
from .discoverWs import InoDriveDiscoverWs
from .userApp import InoDriveUserApp


class InoDrive(object):
    def __init__(self, **kwargs):
        logging.debug('Create InoDrive instance...')
        self._auto_connect = kwargs.get('autoConnect', False)

        self._connection_handle = InoDriveWS(**kwargs)
        if self._auto_connect:
            self._connection_handle.connect()

        self._id_file = InoDriveFile(connection_handle=self._connection_handle, **kwargs)
        self._id_discover = InoDriveDiscoverWs(connection_handle=self._connection_handle, **kwargs)
        self._id_user_app = InoDriveUserApp(connection_handle=self._connection_handle, **kwargs)
        logging.debug('Instance created...')

    def __del__(self):
        self.dispose()

    def dispose(self):
        if self._id_user_app:
            self._id_user_app.dispose()

        if self._connection_handle:
            self._connection_handle.dispose()

    def connect(self, timeout=None):
        return self._connection_handle.connect(timeout)

    def disconnect(self, timeout=None):
        return self._connection_handle.disconnect(timeout)

    def set_target(self, target=None):
        if self._connection_handle:
            self._connection_handle.set_target(target)

    def get_discover_info(self, *args, **kwargs):
        return self._id_discover.discover(*args, **kwargs)

    def delete_uapp(self):
        return self._id_file.delete_uapp()

    def file_read(self, *args, **kwargs):
        return self._id_file.read(*args, **kwargs)

    def file_write(self, *args, **kwargs):
        return self._id_file.write(*args, **kwargs)

    def upload_user_app(self, content=None):
        try:
            return self.file_write({'path': "/uapp/application.idsol", 'content': content}, CK.FILE.UAPP_TRANSFER)
        except Exception as ex:
            logging.exception(ex)

    def upload_firmware(self, content=None):
        try:
            return self.file_write({'path': "/firmware/firmware.nhfw", 'content': content}, CK.FILE.FIRMWARE_TRANSFER)
        except Exception as ex:
            logging.exception(ex)

    # User Application Poll
    def start_poll(self, *args, **kwarg):
        return self._id_user_app.start_poll(*args, **kwarg)

    def stop_poll(self):
        return self._id_user_app.stop_poll()

    def get_variable_list(self, *args, **kwargs):
        return self._id_user_app.get_variable_list(*args, **kwargs)

    def get_variable(self, *args, **kwargs):
        return self._id_user_app.get_variable(*args, **kwargs)

    def get_all_variables(self, *args, **kwargs):
        return self._id_user_app.get_all_variables(*args, **kwargs)

    def read_var(self, *args, **kwargs):
        return self._id_user_app.read_var(*args, **kwargs)

    def write_var(self, *args, **kwargs):
        return self._id_user_app.write_var(*args, **kwargs)

    def get_var(self, *args, **kwargs):
        return self._id_user_app.get_var(*args, **kwargs)

    def set_var(self, *args, **kwargs):
        return self._id_user_app.set_var(*args, **kwargs)
