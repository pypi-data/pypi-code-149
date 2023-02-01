#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) THL A29 Limited, a Tencent company. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0
#
# @FileName     :   crypto_config_utils.py
# @Function     :   crypto_config实用方法，获取对应的授权模式，获取节点nodeid, 获取用户对象、创建背书等
import os
import re
from collections import ChainMap
from pathlib import Path
from typing import Dict, List, Union

import yaml

from chainmaker.chain_client import ChainClient, ChainClientWithEndorsers
from chainmaker.keys import AuthType, Role, HashType, AddrType
from chainmaker.node import Node
from chainmaker.sdk_config import DefaultConfig
from chainmaker.user import User
from chainmaker.utils import file_utils
from chainmaker.utils.file_utils import load_yaml

DEFAULT_ENDORSERS_CNT = 0
DEFAULT_CONN_CNT = 1
DEFAULT_PK_USER = 'admin1@node1'
DEFAULT_CERT_USER = 'client1@wx-org1.chainmaker.org'
DEFAULT_PWK_USER = 'admin@wx-org1.chainmaker.org'
DEFAULT_CRYPTO = {'hash': HashType.SHA256.name}
DEFAULT_TLS_HOME_NAME = 'chainmaker.org'
DEFAULT_ARCHIVE_CONFIG = {'dest': 'root:passw0rd:localhost:3306', 'secret_key': 'passw0rd', 'type': 'mysql'}
DEFAULT_RPC_CLIENT_CONFIG = {'rpc_max_send_message_length': DefaultConfig.rpc_max_send_message_length,
                             'rpc_max_receive_message_length': DefaultConfig.rpc_max_receive_message_length}
DEFAULT_PKCS_CONFIG = None
DEFAULT_HOST = '127.0.0.1'
DEFAULT_RPC_START_PORT = 12301
DEFAULT_SDK_CONFIG_NODE_CNT = 4


def guess_role(name: str) -> str:
    return re.sub(r'\d+', '', name)


def get_org_short_id(org_id: str):  # 未使用
    return org_id.lstrip('wx-').rstrip('.chainmaker.org')


def get_user_short_name(name: str, org_id_or_node_name: str):
    sn, = re.findall(r'\d+', org_id_or_node_name) or ['']
    return '%s%s' % (guess_role(name), sn)


def guess_name_role_and_node(sign_key_file, auth_type) -> (str, Role, str):
    """
    不严谨：从标准crypto_config的用户签名私钥路径中解析用户名、角色及所在节点
    :param user_sign_key_file_path: 用户签名私钥路径
    :param auth_type: 授权类型
    :return: (用户名称,角色,所在节点)
    """
    if auth_type == AuthType.Public:
        m = re.match(r'.*/(?P<node>node\d+)/(?P<name>\w+).*key', sign_key_file)
    else:
        m = re.match(r'.*/(?P<name>\w+).*key', sign_key_file)
    if m:
        node = m.group('node') if auth_type == AuthType.Public else None
        name = m.group('name')
        role = re.sub(r'\d+', '', name)
        return name, role, node
    return '' * 3


def download_dir_from_host(host, port, user, password, remote_dir, local_dir):
    import paramiko
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=port, username=user, password=password)
    sftp = ssh.open_sftp()

    remote_dir_parent, remote_dir_base = os.path.dirname(remote_dir), os.path.basename(remote_dir)
    local_dir_parent, local_dir_base = os.path.dirname(local_dir), os.path.basename(local_dir)

    # 服务端压缩文件
    zip_file = '%s.zip' % remote_dir_base
    ssh.exec_command(f"cd {remote_dir_parent} && zip -r {zip_file} {remote_dir_base}/*")

    # 下载压缩文件
    remote_file, local_file = '%s.zip' % remote_dir, '%s.zip' % local_dir
    sftp.get(remote_file, local_file)

    # 删除服务端压缩文件
    ssh.exec_command('rm -f %s' % remote_file)

    # 解压本地压缩文件
    os.system(f'cd {local_dir_parent} && unzip {zip_file} && cd -')
    # 删除本地压缩文件
    os.remove(local_file)
    ssh.close()


class CryptoBase:
    def __init__(self, crypto_dir: Path, auth_type: AuthType, org_id_or_node_name: str, key: str = None):
        self.crypto_dir = crypto_dir
        self.auth_type = auth_type

        self.name = crypto_dir.name
        self.role = guess_role(self.name)
        self.full_name = f'{self.name}@{org_id_or_node_name}'
        self.key = key or get_user_short_name(self.name, org_id_or_node_name)

        if auth_type == AuthType.PermissionedWithCert:
            self.sign_key_file = str(crypto_dir / f'{self.name}.sign.key')
            self.sign_cert_file = str(crypto_dir / f'{self.name}.sign.crt')
            self.tls_key_file = str(crypto_dir / f'{self.name}.tls.key')
            self.tls_cert_file = str(crypto_dir / f'{self.name}.tls.crt')
        else:
            self.sign_key_file = str(crypto_dir / f'{self.name}.key')
            self.sign_cert_file = str(crypto_dir / f'{self.name}.pem')
            self.user_addr_file = str(crypto_dir / f'{self.name}.addr')

        if auth_type != AuthType.Public:
            self.org_id = org_id_or_node_name
            self.ca_path = crypto_dir.parent.parent / 'ca'
            self.org_ca_key_file = self.ca_path / 'ca.key'
            self.org_ca_cert_file = self.ca_path / 'ca.crt'

    @property
    def sign_key_bytes(self) -> bytes:
        return file_utils.read_file_bytes(self.sign_key_file)

    @property
    def sign_cert_bytes(self) -> bytes:
        return file_utils.read_file_bytes(self.sign_cert_file)

    @property
    def tls_key_bytes(self) -> bytes:
        return file_utils.read_file_bytes(self.tls_key_file)

    @property
    def tls_cert_bytes(self) -> bytes:
        return file_utils.read_file_bytes(self.tls_cert_file)

    @property
    def org_ca_cert_bytes(self) -> bytes:
        return file_utils.read_file_bytes(self.org_ca_cert_file)

    @property
    def trust_root_crt(self) -> str:
        return self.org_ca_cert_bytes.decode()

    @property
    def org_ca_key_bytes(self) -> bytes:
        return file_utils.read_file_bytes(self.org_ca_key_file)

    def _create_client_node(self, host: str = DEFAULT_HOST, start_rpc_port=DEFAULT_RPC_START_PORT):
        node_addr = '%s:%d' % (host, start_rpc_port)
        if self.auth_type == AuthType.PermissionedWithCert:
            node = Node.from_conf(node_addr, DEFAULT_CONN_CNT, True, [str(self.ca_path)],
                                  DEFAULT_TLS_HOME_NAME)
        else:
            node = Node.from_conf(node_addr, DEFAULT_CONN_CNT)
        return node

    def to_client_user(self, hash_type: HashType = None, alias: str = None, addr_type: AddrType = None) -> User:
        return User(org_id=self.org_id, sign_key_bytes=self.sign_key_bytes, sign_cert_bytes=self.sign_cert_bytes,
                    tls_key_bytes=self.tls_key_bytes, tls_cert_bytes=self.tls_cert_bytes,
                    auth_type=self.auth_type, hash_type=hash_type, alias=alias)

    def new_chain_client(self, chain_id='chain1', host: str = DEFAULT_HOST, start_rpc_port=DEFAULT_RPC_START_PORT,
                         hash_type: HashType = None, alias: str = None, addr_type: AddrType = None) -> ChainClient:
        user = self.to_client_user(hash_type, alias, addr_type)
        node = self._create_client_node(host, start_rpc_port)
        return ChainClient(chain_id, user, [node])

    # @property
    # def _cc(self):
    #     return ChainManager.from_conf(self._sdk_config)
    #
    # @property
    # def endorsers(self) -> List[ClientUser]:
    #     return self._cc.endorsers
    #
    # @endorsers.setter
    # def endorsers(self, endorsers: List["ChainUser"]):
    #     endorsers = [user._cc.user for user in endorsers]
    #     self._cc.endorsers = endorsers


# class CryptoConfigOrg:
#     def __init__(self, org_id: str, org_dir: Path):
#         self.org_id = org_id
#         self.ca_path = org_dir / 'ca'
#         self.ca_key_file = self.ca_path / 'ca.key'
#         self.ca_cert_file = self.ca_path / 'ca.crt'
#
#     @property
#     def ca_key_bytes(self) -> bytes:
#         return file_utils.read_file_bytes(self.ca_key_file)
#
#     @property
#     def ca_cert_bytes(self) -> bytes:
#         return file_utils.read_file_bytes(self.ca_cert_file)
#
#     @property
#     def ca_key(self) -> Sm2PrivateKey:
#         return crypto_utils.load_pem_private_key(self.ca_key_bytes)
#
#     @property
#     def ca_cert(self) -> Certificate:
#         return crypto_utils.load_pem_cert(self.ca_cert_bytes)


class CryptoConfigUser(CryptoBase):
    def __init__(self, crypto_dir: Path, auth_type: AuthType, org_id_or_node_name: str = None, key: str = None):
        super().__init__(crypto_dir, auth_type, org_id_or_node_name, key=key)
        if auth_type == AuthType.PermissionedWithCert:
            self.enc_key_file = str(crypto_dir / f'{self.name}.enc.key')
            self.enc_cert_file = str(crypto_dir / f'{self.name}.enc.crt')

    def __repr__(self):
        return '<CryptoConfigUser %s>' % self.full_name

    @property
    def enc_key_bytes(self) -> bytes:
        return file_utils.read_file_bytes(self.enc_key_file, ignore_io_error=True)

    @property
    def enc_cert_bytes(self) -> bytes:
        return file_utils.read_file_bytes(self.enc_cert_file, ignore_io_error=True)


class CryptoConfigNode(CryptoBase):
    def __init__(self, crypto_dir: Path, auth_type: AuthType, org_id_or_node_name: str = None):
        """
        客户端连接节点
        :param node_addr: 必须, 节点RPC地址，eg. 127.0.0.1:12301
        :param conn_cnt: 创建连接数量，默认为1
        :param conn_node: 节点索引
        :param enable_tls: 是否启用tls
        :param trust_root_paths: ca证书二进制内容列表，或ca证书二进制列表连接成的byte字符串
        :param tls_host_name: tls服务器名称
        :param org_id: [额外] 节点所属组织Id
        :param org_ca_key_file: [额外]节点所属组织CA私钥文件路径
        :param org_ca_cert_file: [额外]节点所属组织CA证书文件路径
        :param sign_key_file: [额外]节点所签名密钥文件路径
        :param sign_cert_file: [额外]节点所签名证书文件路径
        :param tls_cert_file: [额外]节点所TLS证书文件路径
        :param tls_cert_file: [额外]节点所TLS证书文件路径
        :param node_id_file: [额外]节点nodeid文件路径
        :param node_name: [额外]节点名称,用于标识节点
        :param node_role: [额外]节点角色,用于标识节点
        """
        super().__init__(crypto_dir, auth_type, org_id_or_node_name)
        self.node_id_file = crypto_dir / f'{self.name}.nodeid'

    def __repr__(self):
        return '<CryptoConfigNode %s>' % self.full_name

    @property
    def node_id(self) -> str:
        return file_utils.read_file(self.node_id_file)


class BaseCryptoConfig:
    def __init__(self, crypto_config_path: Union[Path, str], host: str = DEFAULT_HOST, rpc_start_port=12301,
                 chainmaker_cryptogen_path: Union[Path, str] = None, node_cnt: int = None):
        assert os.path.isdir(crypto_config_path), f'目录不存在：{crypto_config_path}'
        self.crypto_config_path = Path(crypto_config_path)
        self.host = host
        self.rpc_start_port = rpc_start_port
        self.chainmaker_cryptogen_path = chainmaker_cryptogen_path
        self.node_cnt = node_cnt or DEFAULT_SDK_CONFIG_NODE_CNT

    def _guess_auth_type(self) -> AuthType:
        if 'node1' in os.listdir(self.crypto_config_path):
            return AuthType.Public
        org1_dir = os.path.join(self.crypto_config_path, 'wx-org1.chainmaker.org')
        if 'admin' in os.listdir(org1_dir):
            return AuthType.PermissionedWithKey
        return AuthType.PermissionedWithCert

    @classmethod
    def from_host(cls, host, port, user, password, chainmaker_go_path, config_dir=''):
        # 下载
        crypto_config_path = os.path.abspath(os.path.join(config_dir, 'crypto-config'))
        if not os.path.isdir(crypto_config_path):
            download_dir_from_host(host, port, user, password,
                                   f'{chainmaker_go_path}/build/crypto-config', crypto_config_path)
        return cls(crypto_config_path, host=host)

    @property
    def auth_type(self) -> AuthType:
        return self._guess_auth_type()

    @property
    def org_or_node_cnt(self) -> int:
        """组织或节点数量"""
        return len(self._org_or_node_dirs)

    @property
    def nodes(self) -> Dict[str, CryptoConfigNode]:
        if self.auth_type in [AuthType.PermissionedWithCert, AuthType.PermissionedWithKey]:
            return self._load_cert_or_pwk_nodes()
        else:
            return self._load_pk_nodes()

    @property
    def users(self) -> Dict[str, CryptoConfigUser]:
        if self.auth_type == AuthType.PermissionedWithCert:
            return self._load_cert_users()
        if self.auth_type == AuthType.Public:
            return self._load_pk_users()
        return self._load_pwk_users()

    @property
    def _org_or_node_dirs(self) -> list:
        """
        获取crypto_config所有子目录
        :return:
        """
        return sorted([dir_name for dir_name in os.listdir(self.crypto_config_path) if
                       dir_name.startswith('wx') or dir_name.startswith('node')],
                      key=lambda x: int(x.lstrip('node').lstrip('wx-org').rstrip('.chainmaker.org')))

    def get_user(self, user_key: str) -> CryptoConfigUser:
        """
        从crypto-config中用户相对路径获取用户对象
        :param user_key: 用户标识 eg. 'client2'
        """
        # name, sn = user_key[:-1], user_key[-1]
        # name = '%s1' % name
        # if self.auth_type != AuthType.Public:
        #     org_id = 'wx-org%s.chainmaker.org' % sn
        # else:
        #     org_id = 'node%s' % sn

        return self.users.get(user_key)

    def get_node(self, node_key: str) -> CryptoConfigNode:
        return self.nodes.get(node_key)

    def _load_users_from_dir(self, users_dir: Path, org_id_or_node_name: str = None, with_key: bool = False):
        users = {}
        for user_dir in (users_dir).iterdir():
            if user_dir.is_dir():
                if with_key:
                    user = CryptoConfigUser(user_dir, self.auth_type, org_id_or_node_name,
                                            key=os.path.basename(user_dir))
                else:
                    user = CryptoConfigUser(user_dir, self.auth_type, org_id_or_node_name)
                users[user.key] = user
        return users

    def _create_node_config(self, enable_tls: bool = False, node_cnt: int = None) -> List[dict]:
        node_cnt = node_cnt or self.node_cnt
        if enable_tls is True:
            return [
                {'node_addr': '%s:%d' % (self.host, self.rpc_start_port + index), 'conn_cnt': DefaultConfig.conn_cnt,
                 'enable_tls': True, 'tls_host_name': DefaultConfig.tls_home_name,
                 'trust_root_paths': ['%s/%s/ca' % (self.crypto_config_path, org_id)]}
                for index, org_id in enumerate(self._org_or_node_dirs[:node_cnt])]
        return [{'node_addr': '%s:%d' % (self.host, self.rpc_start_port + index), 'conn_cnt': DefaultConfig.conn_cnt}
                for index, org_id in enumerate(self._org_or_node_dirs[:node_cnt])]

    def _get_crypto_dir(self, user_or_node: str) -> (str, str, str):
        """
        获取用户证书路径
        :param user_or_node: 用户标识
            cert模式: client2 ==> 'client1@wx-org2.chainmaker.com', common1 ==> 'common@wx-org1.chainmaker.com'
            pk模式: client2 ==> 'client1@node2'  admin2 ==> 'admin2@node1'
            pwk模式: admin1 ==>  'admin@wx-org1.chainmaker.com', 'admin_user1' ==> 'admin1@wx-org1.chainmaker.com'
        :return:
        """
        user_full_name = self._user_key_to_full_name(user_or_node)
        dir_name, org_id = user_full_name.split('@')
        role = re.sub(r'\d+', '', dir_name)
        if self.auth_type == AuthType.PermissionedWithCert:
            if role in ['client', 'admin', 'light']:
                crypto_dir = f'{self.crypto_config_path}/{org_id}/user/{dir_name}'
            else:
                crypto_dir = f'{self.crypto_config_path}/{org_id}/node/{dir_name}'
        elif self.auth_type == AuthType.PermissionedWithKey:
            if role == 'admin':
                crypto_dir = f'{self.crypto_config_path}/{org_id}/admin'
                dir_name = 'admin'
            elif role in ['client', 'admin_user', 'light']:
                dir_name = dir_name.replace('_user', '')
                crypto_dir = f'{self.crypto_config_path}/{org_id}/user/{dir_name}'
            else:
                crypto_dir = f'{self.crypto_config_path}/{org_id}/node/{dir_name}'

        else:  # todo  pk / pwk admin
            if role == 'client':
                crypto_dir = f'{self.crypto_config_path}/{org_id}/user/{dir_name}'
            else:
                crypto_dir = f'{self.crypto_config_path}/node1/admin/{dir_name}'
        return org_id, dir_name, crypto_dir


class CryptoConfigPublic(BaseCryptoConfig):
    def _load_pk_nodes(self) -> Dict[str, CryptoConfigNode]:
        nodes = {}
        for node_name in self._org_or_node_dirs:
            node_dir = self.crypto_config_path / node_name
            node = CryptoConfigNode(node_dir, self.auth_type, node_name)
            nodes[node.key] = node
        return nodes

    def _load_pk_users(self) -> Dict[str, CryptoConfigUser]:
        users = {}
        for node_name in self._org_or_node_dirs:
            node_dir = self.crypto_config_path / node_name
            # 加载管理员用户 admin/admin1 - adminN
            if node_name == 'node1':  # 由于不同节点的admins都一样，仅加载node1中都admins
                users.update(self._load_users_from_dir(node_dir / 'admin', node_name, with_key=True))

            # 加载普通用户
            users.update(self._load_users_from_dir(node_dir / 'user', node_name))

        return users

    def _create_pk_sdk_config(self, user_full_name: str = None, endorsers_cnt: int = None, endorsers: List[str] = None,
                              alias: str = None, chain_id=DefaultConfig.chain_id, node_cnt: int = 4) -> dict:
        user_full_name = user_full_name or DEFAULT_PK_USER
        _, dir_name, crypto_dir = self._get_crypto_dir(user_full_name)
        chain_client = {'chain_id': chain_id, 'archive': DEFAULT_ARCHIVE_CONFIG}
        chain_client.update({
            'user_sign_key_file_path': f"{crypto_dir}/{dir_name}.key",
            'crypto': DEFAULT_CRYPTO,
            'auth_type': 'public',
            'nodes': self._create_node_config(enable_tls=False, node_cnt=node_cnt), }
        )
        if alias is not None:
            chain_client['alias'] = alias

        # 额外-背书用户配置
        chain_client['endorsers'] = self._create_pk_endorsers(endorsers_cnt=endorsers_cnt, endorsers=endorsers)
        return dict(chain_client=chain_client)

    def _create_pk_endorsers(self, endorsers_cnt: int = None, endorsers: List[str] = None) -> List[dict]:
        """创建pk模式默认背书"""
        if endorsers is None and isinstance(endorsers_cnt, int) and endorsers_cnt > 0:
            return [
                {'auth_type': 'public',
                 'user_sign_key_file_path': f"{self.crypto_config_path}/{node}/admin/admin{index + 1}"
                                            f"/admin{index + 1}.key"}
                for index, node in enumerate(self._org_or_node_dirs[:endorsers_cnt])]
        endorsers_config = []
        for user_key in (endorsers or []):
            user = self.get_user(user_key) or self.get_node(user_key)
            endorsers_config.append({'auth_type': 'public',
                                     'user_sign_key_file_path': user.sign_key_file})
        return endorsers_config


class CryptoConfigPermissionedWithCert(BaseCryptoConfig):
    def _load_cert_or_pwk_nodes(self) -> Dict[str, CryptoConfigNode]:
        nodes = {}
        for org_id in self._org_or_node_dirs:
            for node_dir in (self.crypto_config_path / org_id / 'node').iterdir():
                node = CryptoConfigNode(node_dir, self.auth_type, org_id)
                nodes[node.key] = node
        return nodes

    def _load_cert_users(self) -> Dict[str, CryptoConfigUser]:
        users = {}
        for org_id in self._org_or_node_dirs:
            users.update(self._load_users_from_dir(self.crypto_config_path / org_id / 'user', org_id))
        return users

    def _create_cert_endorsers(self, endorsers_cnt: int = None, endorsers: List[str] = None) -> List[dict]:
        """创建cert模式默认背书"""
        if endorsers is None and isinstance(endorsers_cnt, int) and endorsers_cnt > 0:
            return [
                {'org_id': org_id,
                 'user_sign_key_file_path': f"{self.crypto_config_path}/{org_id}/user/admin1/admin1.sign.key",
                 'user_sign_crt_file_path': f"{self.crypto_config_path}/{org_id}/user/admin1/admin1.sign.crt"}
                for org_id in self._org_or_node_dirs[:endorsers_cnt]]
        endorsers_config = []
        for user_key in (endorsers or []):
            user = self.get_user(user_key) or self.get_node(user_key)
            endorsers_config.append({'org_id': user.org_id,
                                     'user_sign_key_file_path': user.sign_key_file,
                                     'user_sign_crt_file_path': user.sign_cert_file})
        return endorsers_config

    def _create_cert_sdk_config(self, user_full_name: str = None, endorsers_cnt: int = None,
                                endorsers: List[str] = None,
                                alias: str = None, chain_id=DefaultConfig.chain_id, node_cnt: int = 4) -> dict:
        user_full_name = user_full_name or DEFAULT_CERT_USER
        org_id, dir_name, crypto_dir = self._get_crypto_dir(user_full_name)

        chain_client = {'chain_id': chain_id, 'archive': DEFAULT_ARCHIVE_CONFIG}
        chain_client.update(
            {'org_id': org_id,
             'user_crt_file_path': f'{crypto_dir}/{dir_name}.tls.crt',
             'user_key_file_path': f'{crypto_dir}/{dir_name}.tls.key',
             'user_sign_crt_file_path': f'{crypto_dir}/{dir_name}.sign.crt',
             'user_sign_key_file_path': f'{crypto_dir}/{dir_name}.sign.key',
             'nodes': self._create_node_config(enable_tls=True, node_cnt=node_cnt), }
        )
        if alias is not None:
            chain_client['alias'] = alias

        # 额外-背书用户配置
        chain_client['endorsers'] = self._create_cert_endorsers(endorsers_cnt=endorsers_cnt, endorsers=endorsers)
        return dict(chain_client=chain_client)


class CryptoConfigPermissionedWithKey(BaseCryptoConfig):
    def _load_pwk_users(self) -> Dict[str, CryptoConfigUser]:
        users = {}
        for org_id in self._org_or_node_dirs:
            org_dir = self.crypto_config_path / org_id
            # 加载admin用户
            user_dir = org_dir / 'admin'
            user = CryptoConfigUser(user_dir, self.auth_type, org_id)
            users[user.key] = user

            # 加载普通用户
            users.update(self._load_users_from_dir(self.crypto_config_path / org_id / 'user', org_id))

        return users

    def _create_pwk_endorsers(self, endorsers_cnt: int = None, endorsers: List[str] = None) -> List[dict]:
        """创建pwk模式默认背书"""
        if endorsers is None and isinstance(endorsers_cnt, int) and endorsers_cnt > 0:
            return [{'org_id': org_id,
                     'auth_type': 'permissionedWithKey',
                     'user_sign_key_file_path': f"{self.crypto_config_path}/{org_id}/admin/admin.key"}
                    for org_id in self._org_or_node_dirs[:endorsers_cnt]]
        endorsers_config = []
        for user_key in (endorsers or []):
            user = self.get_user(user_key) or self.get_node(user_key)
            endorsers_config.append({'org_id': user.org_id,
                                     'auth_type': 'permissionedWithKey',
                                     'user_sign_key_file_path': user.sign_key_file})
            return endorsers_config

    def _create_pwk_sdk_config(self, user_full_name: str = None, endorsers_cnt: int = None, endorsers: List[str] = None,
                               alias: str = None, chain_id=DefaultConfig.chain_id, node_cnt: int = 4) -> dict:
        user_full_name = user_full_name or DEFAULT_PWK_USER
        org_id, dir_name, crypto_dir = self._get_crypto_dir(user_full_name)

        chain_client = {'chain_id': chain_id, 'archive': DEFAULT_ARCHIVE_CONFIG}
        chain_client.update({
            'org_id': org_id,
            'user_sign_key_file_path': f"{crypto_dir}/{dir_name}.key",  # todo
            'crypto': DEFAULT_CRYPTO,
            'auth_type': 'permissionedWithKey',
            'nodes': self._create_node_config(enable_tls=False, node_cnt=node_cnt)}
        )
        if alias is not None:
            chain_client['alias'] = alias

        # 额外-背书用户配置
        chain_client['endorsers'] = self._create_pwk_endorsers(endorsers_cnt=endorsers_cnt, endorsers=endorsers)
        return dict(chain_client=chain_client)


class CryptoConfig(CryptoConfigPermissionedWithCert, CryptoConfigPermissionedWithKey, CryptoConfigPublic):

    def __repr__(self):
        return '<CryptoConfig %s>' % self.crypto_config_path

    # @property
    # def clients(self) -> Dict[str, ChainManager]:
    #     clients = {}
    #     for key, user_or_node in ChainMap(self.users, self.nodes).items():
    #         cc = self.new_chain_client(user_or_node.full_name)
    #         clients[user_or_node.key] = cc
    #     return clients

    def _get_sdk_config_path(self) -> Path:
        sdk_config_file = {'PermissionedWithCert': 'sdk_config.yml',
                           'Public': 'sdk_config_pk.yml',
                           'PermissionedWithKey': 'sdk_config_pwk.yml'
                           }.get(self.auth_type.name, 'sdk_config.yml')
        return self.crypto_config_path.parent / sdk_config_file

    def get_user_or_node(self, user_or_node_key: str):
        return ChainMap(self.users, self.nodes).get(user_or_node_key)

    def create_default_endorsers(self, endorsers_cnt: int = None, endorsers: List[str] = None) -> List[dict]:
        """
        当config.yml中未配置背书时，创建默认背书用户
        :param endorsers:
        :param endorsers_cnt:
        :param auth_type: 授权类型 cert_or_cert_bytes 证书模式 / pk public模式 /  pwk Key模式
        """
        if endorsers_cnt is None and endorsers is None:
            return []
        if isinstance(endorsers_cnt, int):
            assert endorsers_cnt <= len(self._org_or_node_dirs), f'背书数量{endorsers_cnt}应少于crypto-config中目录数'
        if self.auth_type == AuthType.PermissionedWithCert:
            return self._create_cert_endorsers(endorsers_cnt, endorsers)
        if self.auth_type == AuthType.Public:
            return self._create_pk_endorsers(endorsers_cnt, endorsers)
        if self.auth_type == AuthType.PermissionedWithKey:
            return self._create_pwk_endorsers(endorsers_cnt, endorsers)

    def create_default_sdk_config(self, user: str = None,
                                  endorsers_cnt: int = None, endorsers: List[str] = None,
                                  alias: str = None,
                                  chain_id=DefaultConfig.chain_id, node_cnt: int = 4) -> dict:
        """
        使用标准crypto-config目录创建一个标准的sdk_config配置
        :param node_cnt:
        :param endorsers:
        :param user: 用户标识 eg. 'client2' or 'client1@wx-org2.chainmaker.org'
        :param alias: 用户证书别名
        :param endorsers_cnt: 背书数量
        :param chain_id: 链Id
        :return: 返回sdk_config字典，同yaml.safe_load(open('sdk_config.yml'))
        """
        if endorsers_cnt is None:
            endorsers_cnt = DEFAULT_ENDORSERS_CNT

        user_full_name = self._user_key_to_full_name(user)

        if self.auth_type == AuthType.PermissionedWithCert:
            return self._create_cert_sdk_config(user_full_name, endorsers_cnt, endorsers, alias, chain_id,
                                                node_cnt=node_cnt)
        if self.auth_type == AuthType.Public:
            return self._create_pk_sdk_config(user_full_name, endorsers_cnt, endorsers, alias, chain_id,
                                              node_cnt=node_cnt)
        if self.auth_type == AuthType.PermissionedWithKey:
            return self._create_pwk_sdk_config(user_full_name, endorsers_cnt, endorsers, alias, chain_id,
                                               node_cnt=node_cnt)

    def create_default_sdk_config_file(self):
        sdk_config_path = self._get_sdk_config_path()
        sdk_config = self.create_default_sdk_config()
        with open(sdk_config_path, 'w') as f:
            yaml.safe_dump(sdk_config, f)
        return sdk_config_path

    def _user_key_to_full_name(self, user_key: str):
        if user_key is None:
            return None
        if '@' in user_key:
            return user_key

        name_chars, sn_chars = [], []
        for ch in user_key:
            if ch.isnumeric():
                sn_chars.append(ch)
            else:
                name_chars.append(ch)
        name = ''.join(name_chars)
        sn = int(''.join(sn_chars))

        if self.auth_type == AuthType.Public:
            return '%s1@node%s' % (name, sn)
        return '%s1@wx-org%s.chainmaker.org' % (name, sn)

    @staticmethod
    def _node_to_node_index(node: Union[str, int] = None):
        if node is None:
            return DefaultConfig.conn_node
        if isinstance(node, int):
            return node

        try:
            sn = int(node.lstrip('node'))
        except Exception:
            raise Exception('node结尾应为数字, eg. "node1"')
        else:
            assert sn > 0, 'node需要应大于0'
            return sn - 1

    def new_chain_client(self, user: str = None, endorsers: List[str] = None, endorsers_cnt: int = None,
                         conn_node: Union[str, int] = None, alias: str = None, enable_cert_hash: bool = False,
                         chain_id=DefaultConfig.chain_id) -> ChainClientWithEndorsers:
        """
        创建带默认背书用户的链客户端
        :param conn_node:
        :param endorsers:
        :param user: 用户标识 eg. 'client2' 或 'client1@wx-org1.chainmaker.org'
        :param alias: 用户证书别名，不为None时启用别名
        :param enable_cert_hash: 为True，且alias为None是启用证书压缩
        :param endorsers_cnt: 携带的背书数量
        :param node: 节点名称或节点索引
        :param chain_id: 链Id
        :return: 链客户端
        """
        node_index = self._node_to_node_index(conn_node)
        sdk_config = self.create_default_sdk_config(user, endorsers_cnt=endorsers_cnt, endorsers=endorsers,
                                                    alias=alias, chain_id=chain_id)
        cc = ChainClientWithEndorsers.from_conf(sdk_config, conn_node=node_index)
        if enable_cert_hash is True and alias is None:
            cc.enable_cert_hash()
        return cc

    def extend_orgs(self, org_cnt=10):
        """扩展组织或node数量"""
        assert self.chainmaker_cryptogen_path is not None, 'chainmaker_cryptogen_path未设置'
        # modify config
        if self.auth_type == AuthType.PermissionedWithCert:
            config_file = f'{self.chainmaker_cryptogen_path}/config/crypto_config_template.yml'
            config = load_yaml(config_file)
            config['crypto_config'][0]['count'] = org_cnt
        elif self.auth_type == AuthType.PermissionedWithKey:
            config_file = f'{self.chainmaker_cryptogen_path}/config/pwk_config_template.yml'
            config = load_yaml(config_file)
            config['pwk_config'][0]['count'] = org_cnt
        else:
            config_file = f'{self.chainmaker_cryptogen_path}/config/pk_config_template.yml'
            config = load_yaml(config_file)
            config['pk_config']['node'][0]['count'] = org_cnt
        with open(config_file, 'w') as f:
            yaml.safe_dump(config, f)

        cmd = (f'cd {self.chainmaker_cryptogen_path}/bin && ./chainmaker-cryptogen extend {self.crypto_config_path} '
               f'-o {self.crypto_config_path}')
        os.system(cmd)


class Orgs:
    org1 = 'wx-org1.chainmaker.org'
    org2 = 'wx-org2.chainmaker.org'
    org3 = 'wx-org3.chainmaker.org'
    org4 = 'wx-org4.chainmaker.org'


class Nodes:
    node1 = 'consensus1@wx-org1.chainmaker.org'
    node2 = 'consensus1@wx-org2.chainmaker.org'
    node3 = 'consensus1@wx-org3.chainmaker.org'
    node4 = 'consensus1@wx-org4.chainmaker.org'


class Users:
    client1 = 'client1'
    client2 = 'client2'
    client3 = 'client3'
    client4 = 'client4'

    admin1 = 'admin1'
    admin2 = 'admin2'
    admin3 = 'admin3'
    admin4 = 'admin4'

    light1 = 'light1'
    light2 = 'light2'
    light3 = 'light3'
    light4 = 'light4'

    consensus1 = 'consensus1@wx-org1.chainmaker.org'
    consensus2 = 'consensus1@wx-org2.chainmaker.org'
    consensus3 = 'consensus1@wx-org3.chainmaker.org'
    consensus4 = 'consensus1@wx-org4.chainmaker.org'

    common1 = 'common1@wx-org1.chainmaker.org'
    common2 = 'common1@wx-org2.chainmaker.org'
    common3 = 'common1@wx-org3.chainmaker.org'
    common4 = 'common1@wx-org4.chainmaker.org'
