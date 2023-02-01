"""
This is kernel module for aiko. It manage resources, run processes and
It is responsble for running aiko based projects.
"""

from .process import process_types_t, process_t
from .message_box import message_box_t


class kernel_t:
    """
    This is aiko kernel class. Each of instance of this class is aiko 
    kernel. Project can have more than one of it, and run it in same time
    on other cores by example. First create instance of it, then add start 
    processes to it, and on end, run scheduler. When scheduler start, 
    processes can create new one, kill other processes or itself, and finaly
    it can call remove on kernel, that stop system
    """

    def __init__(self):
        """
        This function is constructor, it create blank kernel instance.
        :return: New aiko kernel instance 
        """

        self.__processes = {}
        self.__last_changed = set()


    def __check_process_exists(self, process):
        """
        This is private aiko function. This is useable to check that process 
        exists, but not by process pid just process object.
        :process: Process to check that exists
        :return: True - process exists, False - process not exists
        """

        if type(process) != process_t:
            return False

        if not process.get_pid() in self.__processes:
            return False

        return True


    def __run_process(self, process):
        """
        This is private aiko function. This try run given process object. 
        It check that process exists in process dics, check process type 
        and message box if it is nessesary. 
        :process: Process to run
        """
        
        if not self.__check_process_exists(process):
            return

        if process.get_type() != process_types_t.CONTINUOUS:
            if not process.get_message_box().is_readable():
                return

        process.worker(self, process)


    def create_process(self, new_process):
        """
        This function create new process in kernel. That get new process 
        create by process constructor, and puts it to process dict. That
        check, and return false, if process already exists.
        :new_process: New process to add
        :return: True - process create success, False - process create fail
        """

        new_process_pid = new_process.get_pid()

        if new_process_pid in self.__processes:
            return False

        if type(new_process) != process_t:
            return False

        self.__processes[new_process_pid] = new_process
        return True


    def kill_process(self, process_pid):
        """
        This function kill process, by process pid. It can by used by each 
        process to kill other or itself.
        :process_pid: Process pid to kill
        :return: True - process kill success, Fail - process kill fail
        """

        if self.check_pid_empty(process_pid):
            return False

        del(self.__processes[process_pid])
        return True

    
    def check_pid_empty(self, process_pid):
        """
        This function check that process pid is empty, or occupied
        :process_pid: Pid of process to check
        :return: True - pid is empty, False - pid is occupied
        """
        
        return not process_pid in self.__processes


    def scheduler(self):
        """
        This function is aiko scheduler. When project call it, then aiko 
        starts. It run processes, in most optimal way. When processes dict
        is empty, because any process call remove, or before scheduler run
        project not adds any processes to kernel, it return. In every other
        case, it always run.
        """

        while True:
            if not len(self.__processes):
                return

            if len(self.__last_changed):
                last_changed = self.__last_changed.copy()
                self.__last_changed.clear()
                
                for process in last_changed:
                    self.__run_process(process)

                continue

            for process in self.__processes.copy().values():
                self.__run_process(process)


    def trigger_signal(self, signal):
        """
        This function trigger signal in system, that mean signal message
        will be send to all processes that have SIGNAL type.
        :signal: Signal to trigger
        """

        for process in self.__processes.copy().values():
            if process.get_type() == process_types_t.SIGNAL:
                self.__process_message_box_send(process, signal)


    def remove(self):
        """
        This function remove kernel, that mean drop all processes from
        processes dict. When any process call this, scheduler stop, and
        return.
        """

        self.__processes.clear()
        self.__last_changed.clear()


    def __process_message_box_send(self, process, message):
        """
        This is aiko private function. It send message to process message 
        box, but use process object, not pid.
        :process: Process object to send
        :message: Message to send
        :return: True - send success, False - send fail, process not exists
        """

        if not self.__check_process_exists(process):
            return False

        process.get_message_box().send(message)
        self.__last_changed.add(process)

        return True


    def process_message_box_send(self, process_pid, message):
        """
        This function send message to process message box, identyfi process 
        by process pid. Processes use this to communicate.
        :process_pid: Process pid to send
        :message: Message to send
        :return: True - send success, False - send fail, process not exists
        """

        if self.check_pid_empty(process_pid):
            return False

        process = self.__processes[process_pid]

        process.get_message_box().send(message)
        self.__last_changed.add(process)

        return True
