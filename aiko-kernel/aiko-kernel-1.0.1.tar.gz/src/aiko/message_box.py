"""
This store message box, important class for communication between processes.
Kernel use it to determinate which processes would be activate, and for 
processes to work on simple and clean query.
"""

class message_box_t:
    """
    This class is message box, that is useable for sending messages between
    processes. It is auto create with process consturctor and using in all 
    aiko structures.
    """

    def __init__(self):
        """
        This function create new empty message box.
        """

        self.__messages = []
    

    def is_readable(self):
        """
        This function check if there are any data to read.
        :return: True - there is data to read, No - There is no data to read
        """

        return len(self.__messages) > 0


    def send(self, data):
        """
        This function send new data to message box.
        :data: New data to send
        """

        self.__messages.append(data)


    def read(self):
        """
        This function read one item from message box. When there is not any
        item, then return None.
        :return: Latest send item or None when empty
        """

        if not self.is_readable():
            return None

        return self.__messages.pop()


    def show(self):
        """
        This function show latest send item to message box, but not pop it 
        from query. When message box is empty, then return None.
        :return: Latest send item, or None when empty
        """

        if not self.is_readable():
            return None

        return self.__messages[len(self.__messages) - 1]

