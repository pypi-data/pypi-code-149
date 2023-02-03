#!/usr/bin/python3

import argparse
import socket
import threading
import sys
import os
import readline
import signal


# To get the ANSI color codes working on windows, first run
# https://stackoverflow.com/a/54955094
os.system('')

class Style():
    '''
    Store ANSI color codes
    '''
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'

def print_cyan(string :str) :
    '''
    Print an information message (in cyan)
    '''
    print(Style.CYAN + string + Style.RESET)

def show_version() :
    # where is this file located
    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, './VERSION')) as version_file:
        version = version_file.read().strip()
        print_cyan("Simple TCP Client v" + version)

def show_header() :
    print_cyan("""
███████╗████████╗ ██████╗
██╔════╝╚══██╔══╝██╔════╝
███████╗   ██║   ██║     
╚════██║   ██║   ██║     
███████║   ██║   ╚██████╗
╚══════╝   ╚═╝    ╚═════╝
""")
    show_version()

    print_cyan('https://gitlab.cylab.be/cylab/simpletcpclient')
    print('')


def read_socket(sock :socket.socket) :
    '''
    Read and display messages received from server.
    Will run in a background thread...
    '''
    while True :

        data = sock.recv(4096).decode()

        if data == "" :
            print_cyan("Connection closed")

            # Interrupt the main thread
            os.kill(os.getpid(), signal.SIGINT)
            return
        print("\n" + Style.GREEN + data + Style.RESET)



autocomplate_values = [
    'GET ', 'POST ', 'HEAD ', 'Host: ', 'User-Agent: ', 'Connection: ',
    'HELO ', 'MAIL FROM: ', 'RCPT TO: ', 'DATA', 'QUIT']

def completer(text, state):
    '''
    Function used to search auto-complete values
    '''
    matches = [v for v in autocomplate_values if v.startswith(text)]
    if len(matches) == 1 and matches[0] == text:
        # Add space if the current text is the same as the only match
        return "{} ".format(matches[0]) if state == 0 else None
    if state >= len(matches):
        return None
    return matches[state]

def main():
    '''
    Main simple-tcp-client entrypoint
    '''
    show_header()

    # https://docs.python.org/3/library/argparse.html
    parser = argparse.ArgumentParser()
    parser.add_argument('server')
    parser.add_argument('port')
    args = parser.parse_args()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((args.server, int(args.port)))

    print_cyan("Connected to " + args.server + ":" + args.port)
    print("")

    reading_thread = threading.Thread(target=read_socket, args=(sock,))
    # close reading_thread when main thread is stopped
    # https://docs.python.org/3/library/threading.html#threading.Thread.daemon
    # https://stackoverflow.com/a/60042836
    reading_thread.daemon = True
    reading_thread.start()

    # Register our auto-complete function
    readline.set_completer(completer)

    # Use the tab key for completion
    readline.parse_and_bind('tab: complete')

    while True :
        # https://stackoverflow.com/a/65207578
        try:
            data = input("") + "\r\n"
        except KeyboardInterrupt:
            # User interrupted the program with ctrl+c
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
            sys.exit()

        sock.send(data.encode())

if __name__ == "__main__":
    main()
