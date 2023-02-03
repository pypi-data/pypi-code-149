#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdout
from io import StringIO, FileIO, BytesIO
from pathlib import Path
from socket import socket
from urllib.request import urlopen
from tarfile import open
from paramiko import Transport, SSHException, SFTPClient
from git.cmd import Git
from git import Repo

class Tar():
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def src(self):
        kwargs = self.kwargs
        if kwargs.get('version'):
            src = BytesIO(urlopen(f'''http://192.168.21.1:5080/APP/develop/develop/update/industry/crab/dists/crab-{version}.tar.xz''').read())
        if kwargs.get('branch'):
            version = BytesIO(urlopen(f'''http://192.168.21.1:5080/APP/develop/develop/update/industry/crab/heads/{kwargs.get('branch')}.txt''').read()).read().decode()
            src = BytesIO(urlopen(f'''http://192.168.21.1:5080/APP/develop/develop/update/industry/crab/dists/crab-{version}.tar.xz''').read())
        else:
            version = Git().describe(Repo(search_parent_directories=True).head.object.hexsha, tags=True, abbrev=True, always=True, long=True)
            src = FileIO(f'''var/crab-{version}.tar.xz''')
        return src

class Archive():
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __iter__(self):
        kwargs = self.kwargs
        tar = open(mode='r:xz', fileobj=Tar(**kwargs).src())
        for tarinfo in tar.getmembers():
            file = tar.extractfile(tarinfo)
            if file:
                yield (Path(f'''{kwargs.get('directory', '/usr/local/crab/')}{tarinfo.name}'''), file)
        tar.close()

class Client():
    def __init__(self, **kwargs):
        self.kwargs = kwargs

        sock = socket()
        sock.connect((kwargs.get('ip', '192.168.1.200'), kwargs.get('port', 22)))
        transport = Transport(sock)
        transport.start_client()
        try:
            if not kwargs.get('password'):
                raise SSHException
            transport.auth_password(kwargs.get('username', 'root'), kwargs.get('password', 'elite2014'))
        except SSHException:
            transport.auth_none(kwargs.get('username', 'root'))
        self.transport = transport

    def writeArchive(self, files):
        client = SFTPClient.from_transport(self.transport)
        for (path, content) in files:
            try:
                client.chdir(str(path.parent))
            except IOError:
                client.mkdir(str(path.parent))
            client.putfo(content, str(path))
        return self

    def exec(self, commands):
        for command in commands:
            try:
                channel = self.transport.open_session()
                channel.set_combine_stderr(True)
                channel.exec_command(command)
                while True:
                    self.transport.send_ignore()
                    if channel.recv_ready():
                        char = channel.recv(1)
                        stdout.buffer.write(char)
                        if char == b'\n':
                            stdout.flush()
                    if channel.exit_status_ready():
                        break
                channel.close()
            except EOFError:
                pass
        return self

def distcrab(ip='192.168.1.200', port=22, username='root', password=None, version=None, branch=None, directory='/usr/local/crab/'):
    Client(ip=ip, port=port, username=username, password=password).exec([
        '/usr/local/bin/elite_local_stop.sh',
    ]).writeArchive(Archive(version=version, branch=branch, directory=directory)).exec([
        '/bin/sync',
        '/usr/local/bin/elite_local_start.sh',
    ])
