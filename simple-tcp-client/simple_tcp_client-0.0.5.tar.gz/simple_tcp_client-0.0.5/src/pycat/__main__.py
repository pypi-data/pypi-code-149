#!/usr/bin/python3

import argparse
import socket
import threading
import sys
import os

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
        print_cyan("v" + version)

def show_header() :
    print_cyan("""
██████╗ ██╗   ██╗ ██████╗ █████╗ ████████╗
██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗╚══██╔══╝
██████╔╝ ╚████╔╝ ██║     ███████║   ██║   
██╔═══╝   ╚██╔╝  ██║     ██╔══██║   ██║   
██║        ██║   ╚██████╗██║  ██║   ██║   
╚═╝        ╚═╝    ╚═════╝╚═╝  ╚═╝   ╚═╝   
""")
    show_version()

    print_cyan('https://gitlab.cylab.be/cylab/pycat')
    print('')


def read_socket(sock :socket.socket) :
    while True :
        data = sock.recv(4096).decode()
        if data == "" :
            print_cyan("Connection closed by server")
            # https://stackoverflow.com/a/7099229
            os._exit(0)
        print("\n" + Style.GREEN + data + Style.RESET)

def main():
    '''
    Main PyCat method
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

    reading_thread = threading.Thread(target=read_socket, args=(sock,))
    reading_thread.start()

    while True :
        # https://stackoverflow.com/a/65207578
        try:
            data = input("") + "\r\n"
        except KeyboardInterrupt:
            # User interrupt the program with ctrl+c
            sys.exit()

        sock.send(data.encode())

if __name__ == "__main__":
    main()
