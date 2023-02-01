"""
This is module for storing processes. It is useable for kernel, it manage 
and protect private processes attributes.
"""

from enum import Enum
from .message_box import message_box_t


class process_types_t(Enum):
    """
    This enum store available process state. When system selecting process
    state, must use this enum.
    """

    REACTIVE = 0
    CONTINUOUS = 1
    SIGNAL = 2


class process_t:
    """
    This class is process container. This store single process, and message
    box for it. Process pid, type and message_box is type is privta, and
    must using getters.
    """

    def __init__(self, process_pid, process_type, worker, parameter):
        """
        This function create new process instance, from parameters.
        :process_pid: This is pid of the new process
        :process_type: This is type of new process, selected from enum
        :worker: Process worker function
        :parameter: Process parameter
        :return: New process instance
        """

        self.__process_pid = process_pid
        self.__message_box = message_box_t()
        self.__process_type = process_type
        self.worker = worker
        self.parameter = parameter


    def get_message_box(self):
        """
        This is useable for working on process message box. Message box is 
        private, because it is very important for working, and any process
        must not managing it.
        :return: Process message box
        """

        return self.__message_box


    def get_pid(self):
        """
        This function return process pid. It is very important, any process
        must not changing it.
        :return: Process pid
        """

        return self.__process_pid


    def get_type(self):
        """
        This function return process type. It is private function, because it
        is very important, and any process must not changing it.
        :return: Process type
        """

        return self.__process_type
