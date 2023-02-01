#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) THL A29 Limited, a Tencent company. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0
#
# @FileName     :   node_server_utils.py
# @Function     :   chainmaker节点服务实用方法
import logging
import re
import threading
import time
from typing import List, Union

from chainmaker.utils.crypto_config_utils import CryptoConfigNode

try:
    from hostz import Host
except ImportError:
    print('please install hostz: pip install hostz')


class ChainMakerNode:
    """长安链服务节点"""

    def __init__(self, index: int, host: Host, release_path: str, rpc_port: int = None,
                 crypto_config_node: CryptoConfigNode = None):
        self.index = index
        self.host = host
        self.release_path = release_path.rstrip('/')
        self.name = f'node{index + 1}'
        self.org_id = self._guess_org_id_from_release_path(self.release_path)
        self.rpc_port = rpc_port or 12301 + index
        self.crypto_config_node = crypto_config_node

        self._bin_path = '%s/bin' % self.release_path
        self._bc1_yml_path = '%s/config/%s/chainconfig/bc1.yml' % (self.release_path, self.org_id)
        self._bc1_yml_bak_path = self._bc1_yml_path.replace('bc1.yml', 'bc1_bak.yml')
        self._chainmaker_yml_path = '%s/config/%s/chainmaker.yml' % (self.release_path, self.org_id)
        self._chainmaker_yml_bak_path = self._chainmaker_yml_path.replace('chainmaker.yml', 'chainmaker_bak.yml')
        self._log_yml_path = '%s/config/%s/log.yml' % (self.release_path, self.org_id)
        self._log_yml_bak_path = self._log_yml_path.replace('log.yml', 'chainmaker_bak.yml')
        self._cached_bc1_config = None
        self._cached_chainmaker_config = None

    def __repr__(self):
        return '<ChainMakerNode %s>' % self.name

    @property
    def pid(self) -> Union[None, int]:
        result = self.host.run("lsof -n -i :%s | grep LISTEN | awk '{print $2}'" % self.rpc_port)
        if result:
            return int(result)

    @property
    def is_active(self) -> bool:
        return self.pid is not None

    @property
    def bc1_config(self) -> dict:
        """
        {'account_config': {'default_gas': 0, 'enable_gas': False, 'gas_count': 0},
         'auth_type': 'permissionedWithCert',
         'block': {'block_interval': 10,
                   'block_size': 10,
                   'block_tx_capacity': 100,
                   'tx_timeout': 600,
                   'tx_timestamp_verify': True},
         'chain_id': 'chain1',
         'consensus': {'ext_config': None,
                       'nodes': [{'node_id': ['QmRw3HFFtfKTQ9pXcYGTuSQzsCFLQpNNmmP4bf9txBPYQP'],
                                  'org_id': 'wx-org1.chainmaker.org'},
                                 {'node_id': ['QmVcufiGxrwzjjM7hH96ZsRPxmDEXxBKHPzk4bQRJnvo4s'],
                                  'org_id': 'wx-org2.chainmaker.org'},
                                 {'node_id': ['QmRCztSr9YsWaaWRSjXAodKwXKPcgAvLPnLDKrtoHRjN4u'],
                                  'org_id': 'wx-org3.chainmaker.org'},
                                 {'node_id': ['QmVt7fkkdTDU2mZuWKFxwt3P7hAdEDkCTK1Yme3EwdgNVM'],
                                  'org_id': 'wx-org4.chainmaker.org'}],
                       'type': 3},
         'contract': {'enable_sql_support': False},
         'core': {'enable_conflicts_bit_window': True,
                  'enable_sender_group': False,
                  'tx_scheduler_timeout': 10,
                  'tx_scheduler_validate_timeout': 10},
         'crypto': {'hash': 'SHA256'},
         'disabled_native_contract': None,
         'resource_policies': [{'policy': {'org_list': None,
                                           'role_list': ['admin'],
                                           'rule': 'SELF'},
                                'resource_name': 'CHAIN_CONFIG-NODE_ID_UPDATE'},
                               {'policy': {'org_list': None,
                                           'role_list': ['admin'],
                                           'rule': 'MAJORITY'},
                                'resource_name': 'CHAIN_CONFIG-TRUST_ROOT_ADD'},
                               {'policy': {'org_list': None,
                                           'role_list': ['admin'],
                                           'rule': 'ANY'},
                                'resource_name': 'CHAIN_CONFIG-CERTS_FREEZE'},
                               {'policy': {'org_list': None,
                                           'role_list': None,
                                           'rule': 'ANY'},
                                'resource_name': 'CONTRACT_MANAGE-INIT_CONTRACT'}],
         'sequence': 0,
         'trust_roots': [{'org_id': 'wx-org4.chainmaker.org',
                          'root': ['../config/wx-org1.chainmaker.org/certs/ca/wx-org4.chainmaker.org/ca.crt']},
                         {'org_id': 'wx-org3.chainmaker.org',
                          'root': ['../config/wx-org1.chainmaker.org/certs/ca/wx-org3.chainmaker.org/ca.crt']},
                         {'org_id': 'wx-org2.chainmaker.org',
                          'root': ['../config/wx-org1.chainmaker.org/certs/ca/wx-org2.chainmaker.org/ca.crt']},
                         {'org_id': 'wx-org1.chainmaker.org',
                          'root': ['../config/wx-org1.chainmaker.org/certs/ca/wx-org1.chainmaker.org/ca.crt']}],
         'version': '2040000',
         'vm': {'addr_type': 2,
                'support_list': ['wasmer', 'gasm', 'evm', 'dockergo', 'wxvm']}}
        :return:
        """
        if self._cached_bc1_config is None:
            self._cached_bc1_config = self.host.load_yaml(self._bc1_yml_path)
        return self._cached_bc1_config

    @property
    def chainmaker_config(self) -> dict:
        """
        {'auth_type': 'permissionedWithCert',
         'blockchain': [{'chainId': 'chain1',
                         'genesis': '../config/wx-org1.chainmaker.org/chainconfig/bc1.yml'}],
         'consensus': {'raft': {'async_wal_save': True, 'snap_count': 10, 'ticker': 1}},
         'crypto_engine': 'tjfoc',
         'log': {'config_file': '../config/wx-org1.chainmaker.org/log.yml'},
         'monitor': {'enabled': False, 'port': 14321},
         'net': {'listen_addr': '/ip4/0.0.0.0/tcp/11301',
                 'provider': 'LibP2P',
                 'seeds': ['/ip4/127.0.0.1/tcp/11301/p2p/QmRw3HFFtfKTQ9pXcYGTuSQzsCFLQpNNmmP4bf9txBPYQP',
                           '/ip4/127.0.0.1/tcp/11302/p2p/QmVcufiGxrwzjjM7hH96ZsRPxmDEXxBKHPzk4bQRJnvo4s',
                           '/ip4/127.0.0.1/tcp/11303/p2p/QmRCztSr9YsWaaWRSjXAodKwXKPcgAvLPnLDKrtoHRjN4u',
                           '/ip4/127.0.0.1/tcp/11304/p2p/QmVt7fkkdTDU2mZuWKFxwt3P7hAdEDkCTK1Yme3EwdgNVM'],
                 'tls': {'cert_enc_file': '../config/wx-org1.chainmaker.org/certs/node/consensus1/consensus1.tls.enc.crt',
                         'cert_file': '../config/wx-org1.chainmaker.org/certs/node/consensus1/consensus1.tls.crt',
                         'enabled': True,
                         'priv_enc_key_file': '../config/wx-org1.chainmaker.org/certs/node/consensus1/consensus1.tls.enc.key',
                         'priv_key_file': '../config/wx-org1.chainmaker.org/certs/node/consensus1/consensus1.tls.key'}},
         'node': {'cert_cache_size': 1000,
                  'cert_file': '../config/wx-org1.chainmaker.org/certs/node/consensus1/consensus1.sign.crt',
                  'fast_sync': {'enabled': True, 'min_full_blocks': 10},
                  'kms': {'address': 'kms.tencentcloudapi.com',
                          'enabled': False,
                          'ext_params': '',
                          'is_public': True,
                          'region': 'ap-guangzhou',
                          'sdk_scheme': 'https',
                          'secret_id': '',
                          'secret_key': ''},
                  'org_id': 'wx-org1.chainmaker.org',
                  'pkcs11': {'enabled': False,
                             'hash': 'SHA256',
                             'label': 'HSM',
                             'library': '/usr/local/lib64/pkcs11/libupkcs11.so',
                             'password': 11111111,
                             'session_cache_size': 10,
                             'type': 'pkcs11'},
                  'priv_key_file': '../config/wx-org1.chainmaker.org/certs/node/consensus1/consensus1.sign.key'},
         'pprof': {'enabled': False, 'port': 24321},
         'rpc': {'blacklist': {'addresses': None},
                 'check_chain_conf_trust_roots_change_interval': 60,
                 'gateway': {'enabled': False, 'max_resp_body_size': 16},
                 'max_recv_msg_size': 100,
                 'max_send_msg_size': 100,
                 'port': 12301,
                 'provider': 'grpc',
                 'ratelimit': {'enabled': False,
                               'token_bucket_size': -1,
                               'token_per_second': -1,
                               'type': 0},
                 'subscriber': {'ratelimit': {'token_bucket_size': 100,
                                              'token_per_second': 100}},
                 'tls': {'cert_enc_file': '../config/wx-org1.chainmaker.org/certs/node/consensus1/consensus1.tls.enc.crt',
                         'cert_file': '../config/wx-org1.chainmaker.org/certs/node/consensus1/consensus1.tls.crt',
                         'mode': 'twoway',
                         'priv_enc_key_file': '../config/wx-org1.chainmaker.org/certs/node/consensus1/consensus1.tls.enc.key',
                         'priv_key_file': '../config/wx-org1.chainmaker.org/certs/node/consensus1/consensus1.tls.key'}},
         'scheduler': {'rwset_log': False},
         'storage': {'bigfilter_config': {'fp_rate': 1e-09,
                                          'redishosts_port': '127.0.0.1:6300,127.0.0.1:6301',
                                          'redis_password': 'abcpass',
                                          'tx_capacity': 1000000000},
                     'blockdb_config': {'leveldb_config': {'store_path': '../data/wx-org1.chainmaker.org/block'},
                                        'provider': 'leveldb'},
                     'contract_eventdb_config': {'provider': 'sql',
                                                 'sqldb_config': {'dsn': 'root:password@tcp(127.0.0.1:3306)/',
                                                                  'sqldb_type': 'mysql'}},
                     'disable_block_file_db': False,
                     'disable_contract_eventdb': True,
                     'enable_bigfilter': False,
                     'enable_rwc': True,
                     'historydb_config': {'disable_account_history': True,
                                          'disable_contract_history': True,
                                          'disable_key_history': False,
                                          'leveldb_config': {'store_path': '../data/wx-org1.chainmaker.org/history'},
                                          'provider': 'leveldb'},
                     'logdb_segment_async': False,
                     'logdb_segment_size': 128,
                     'resultdb_config': {'leveldb_config': {'store_path': '../data/wx-org1.chainmaker.org/result'},
                                         'provider': 'leveldb'},
                     'rolling_window_cache_capacity': 55000,
                     'state_cache_config': {'clean_window': 1000000000,
                                            'hard_max_cache_size': 1024,
                                            'life_window': 3000000000000,
                                            'max_entry_size': 500},
                     'statedb_config': {'leveldb_config': {'store_path': '../data/wx-org1.chainmaker.org/state'},
                                        'provider': 'leveldb'},
                     'store_path': '../data/wx-org1.chainmaker.org/ledgerData1',
                     'unarchive_block_height': 300000,
                     'write_block_type': 0},
         'tx_filter': {'birds_nest': {'cuckoo': {'bits_per_item': 11,
                                                 'key_type': 1,
                                                 'max_num_keys': 2000000,
                                                 'table_type': 0,
                                                 'tags_per_bucket': 2},
                                      'length': 10,
                                      'rules': {'absolute_expire_time': 172800},
                                      'snapshot': {'block_height': {'interval': 10},
                                                   'path': '../data/wx-org1.chainmaker.org/tx_filter',
                                                   'serialize_interval': 10,
                                                   'timed': {'interval': 10},
                                                   'type': 0}},
                       'sharding': {'birds_nest': {'cuckoo': {'bits_per_item': 11,
                                                              'key_type': 1,
                                                              'max_num_keys': 2000000,
                                                              'table_type': 0,
                                                              'tags_per_bucket': 2},
                                                   'length': 10,
                                                   'rules': {'absolute_expire_time': 172800}},
                                    'length': 5,
                                    'snapshot': {'block_height': {'interval': 10},
                                                 'path': '../data/wx-org1.chainmaker.org/tx_filter',
                                                 'serialize_interval': 10,
                                                 'timed': {'interval': 10},
                                                 'type': 0},
                                    'timeout': 60},
                       'type': 0},
         'txpool': {'batch_create_timeout': 50,
                    'batch_max_size': 100,
                    'common_queue_num': 8,
                    'is_dump_txs_in_queue': True,
                    'max_config_txpool_size': 10,
                    'max_txpool_size': 50000,
                    'pool_type': 'normal'},
         'vm': {'go': {'contract_engine': {'host': '127.0.0.1',
                                           'max_connection': 5,
                                           'port': 22351},
                       'data_mount_path': '../data/wx-org1.chainmaker.org/go',
                       'dial_timeout': 10,
                       'enable': False,
                       'log_in_console': False,
                       'log_level': None,
                       'log_mount_path': '../log/wx-org1.chainmaker.org/go',
                       'max_concurrency': 20,
                       'max_recv_msg_size': 100,
                       'max_send_msg_size': 100,
                       'protocol': None,
                       'runtime_server': {'port': 32351}}}}
        :return:
        """
        if self._cached_chainmaker_config is None:
            self._cached_chainmaker_config = self.host.load_yaml(self._chainmaker_yml_path)
        return self._cached_chainmaker_config

    def start(self):
        """
        启动节点
        :return: 命令行输出结果
        """
        logging.debug('启动节点: %s' % self.name)
        cmd = f'''echo '
           ' | sh start.sh'''
        output = self.host.run(cmd, workspace=self._bin_path)
        # time.sleep(2)  # 必须等待2秒, 不然重新使用会报错
        return output

    def stop(self, clean=False, stop_vm_container=True):
        """
        停止节点
        :return: 命令行输出结果
        """
        logging.debug('停止节点: %s' % self.name)

        if stop_vm_container is True:
            self.host.run('sh stop.sh full', workspace=self._bin_path)
        else:
            self.host.run('sh stop.sh alone', workspace=self._bin_path)
        if clean is True:
            self._clean()

    def restart(self, clean=False, duration: int = None, reset_config: bool = False):
        """
        重启节点
        :param clean: 清理节点数据及日志  # todo 清理sql数据库
        :param duration: 节点停止后等待时间
        :param reset_config: 是否重置bc1.yml和chainmaker.yml配置
        """
        if reset_config:
            self._reset_config()

        if duration is None:
            if clean:
                self._clean()
            self.host.run('sh restart.sh full', workspace=self._bin_path)
        else:
            self.stop(clean)
            time.sleep(duration)
            self.start()

    def modify_bc1_yml(self, chain_id: str = None, version: str = None, sequence: int = None, auth_type: str = None,
                       crypto: dict = None, contract: dict = None, vm: dict = None, block: dict = None,
                       core: dict = None,
                       account_config: dict = None, consensus: dict = None, trust_roots: List[dict] = None,
                       resource_policies: List[dict] = None, disabled_native_contract: List[str] = None) -> None:
        """
        修改节点bc1.yml配置
        :param chain_id: 链id eg. chain1
        :param version: 链版本 eg. v2.3.0
        :param sequence: 配置序号 eg. 0
        :param auth_type: 授权类型 eg. permissionedWithCert
        :param crypto: 加密配置 eg. {'hash': 'SHA256'}
        :param contract: 合约配置 eg. {'enable_sql_support': False}
        :param vm: 虚拟机配置 eg. {'addr_type': 2, support_list: ['wasmer', 'gasm', 'evm', 'dockergo', 'wxvm']}
        :param block: 区块配置 eg. {'tx_timestamp_verify': True, 'tx_timeout': 600, 'block_tx_capacity': 100,
                                  'block_size': 10, 'block_interval': 10}
        :param core: 核心配置 eg. {'tx_scheduler_timeout':10 , 'tx_scheduler_validate_timeout': 10,
                                 'enable_sender_group': False, 'enable_conflicts_bit_window': True}
        :param account_config: Gas账户配置 eg. {'enable_gas': False, 'gas_count': 0, 'default_gas': 0}
        :param consensus: 共识配置 eg. {'type': 3, 'nodes': [{'org_id': 'wx-org1.chainmaker.org',
                                                            'node_id': ['QmTTayzjbQqzzarWMo9HQSZsnZWLAQz2oefogKZuhbMnfD']}, ...],
                                       'ext_config': None}
        :param trust_roots: 信任组织根证书配置 eg. [{'org_id': 'wx-org1.chainmaker.org',
                                                  'root': ['../config/wx-org1.chainmaker.org/certs/ca/wx-org1.chainmaker.org/ca.crt']}]
        :param resource_policies: 权限配置 eg. [{'resource_name': 'CHAIN_CONFIG-NODE_ID_UPDATE',
                                                'policy': {'rule': 'SELF', org_list: None, role_list: ['admin']}, ...]
        :param disabled_native_contract: 禁用系统合约配置 eg. None
        """
        if chain_id:
            self.bc1_config['chain_id'] = chain_id
        if version:
            self.bc1_config['version'] = version
        if sequence:
            self.bc1_config['sequence'] = sequence
        if auth_type:
            self.bc1_config['auth_type'] = auth_type
        if crypto:
            self.bc1_config['crypto'].update(crypto)
        if contract:
            self.bc1_config['contract'].update(contract)
        if vm:
            self.bc1_config['vm'].update(vm)
        if block:
            self.bc1_config['block'].update(block)
        if core:
            self.bc1_config['core'].update(core)
        if account_config:
            self.bc1_config['account_config'].update(account_config)
        if consensus:
            self.bc1_config['consensus'].update(consensus)
        if trust_roots:
            self.bc1_config['trust_roots'] = trust_roots
        if resource_policies:
            self.bc1_config['resource_policies'] = resource_policies
        if disabled_native_contract:
            self.bc1_config['disabled_native_contract'] = disabled_native_contract

        if not self.host.exists(self._bc1_yml_bak_path):
            self.host.run(f'cp {self._bc1_yml_path} {self._bc1_yml_bak_path}')
        self.host.save_yaml(self.bc1_config, self._bc1_yml_path)
        self._cached_bc1_config = None

    def modify_chainmaker_yml(self, auth_type: str = None, log: dict = None, crypto_engine: str = None,
                              blockchain: List[dict] = None, node: dict = None, net: dict = None, txpool: dict = None,
                              rpc: dict = None, tx_filter: dict = None, monitor: dict = None, pprof: dict = None,
                              consensus: dict = None, scheduler: dict = None, storage: dict = None, vm: dict = None):
        """
        修改节点chainmaker.yml配置
        :param auth_type: 节点授权模式 eg. permissionedWithCert
        :param log: 节点日志配置 eg. {'config_file': '../config/wx-org1.chainmaker.org/log.yml'}
        :param crypto_engine: 节点国密引擎配置, 支持gmssl,tencentsm和tjfoc eg. tjfoc
        :param blockchain: 节点链配置 eg. [{'chainId: 'chain1', 'genesis': '../config/wx-org1.chainmaker.org/chainconfig/bc1.yml'}]
        :param node: 节点配置 eg. {'org_id': 'wx-org1.chainmaker.org', 'priv_key_file': '../config/wx-org1.chainmaker.org/certs/node/consensus1/consensus1.sign.key',
                                  'cert_file': '../config/wx-org1.chainmaker.org/certs/node/consensus1/consensus1.sign.crt',
                                  'cert_cache_size': 1000, 'cert_key_usage_check': True,
                                  'fast_sync': {'enabled: True, 'min_full_blocks': 10},
                                  'pkcs11': {'enabled': False, 'type': 'pkcs11', 'library': '/usr/local/lib64/pkcs11/libupkcs11.so',
                                             'label': 'HSM', 'password': '11111111', 'session_cache_size': 10, 'hash': 'SHA256'}}
        :param net: 节点网络配置 eg. {'provider': 'LibP2P','listen_addr': '/ip4/0.0.0.0/tcp/11301',
                                    'seeds': ['/ip4/127.0.0.1/tcp/11301/p2p/QmTTayzjbQqzzarWMo9HQSZsnZWLAQz2oefogKZuhbMnfD', ...],
                                    'tls': {'enabled': True, 'priv_key_file': '...', 'cert_file': '...', 'priv_enc_key_file': '...',
                                            'cert_enc_file': '...'}}
        :param txpool: 节点交易池配置 eg. {'pool_type': 'normal', 'max_txpool_size': 50000, 'max_config_txpool_size': 10,
                                         'is_dump_txs_in_queue': true, 'common_queue_num': 8, 'batch_max_size': 100,
                                         'batch_create_timeout': 50}
        :param rpc: 节点rpc配置 eg. {'blacklist': {'addresses': None},
                                    'check_chain_conf_trust_roots_change_interval': 60,
                                    'gateway': {'enabled': False, 'max_resp_body_size': 16},
                                    'max_recv_msg_size': 100,'max_send_msg_size': 100, 'port': 12301,'provider': 'grpc',
                                    'ratelimit': {'enabled': False,'token_bucket_size': -1,'token_per_second': -1,'type': 0},
                                    'subscriber': {'ratelimit': {'token_bucket_size': 100,'token_per_second': 100}},
                                    'tls': {'cert_enc_file': '../config/wx-org1.chainmaker.org/certs/node/consensus1/consensus1.tls.enc.crt',
                                            'cert_file': '../config/wx-org1.chainmaker.org/certs/node/consensus1/consensus1.tls.crt',
                                            'mode': 'twoway',
                                            'priv_enc_key_file': '../config/wx-org1.chainmaker.org/certs/node/consensus1/consensus1.tls.enc.key',
                                            'priv_key_file': '../config/wx-org1.chainmaker.org/certs/node/consensus1/consensus1.tls.key'}}
        :param tx_filter: 节点交易过滤器配置 eg. {'birds_nest': {'cuckoo': {'bits_per_item': 11, 'key_type': 1, 'max_num_keys': 2000000,'table_type': 0,'tags_per_bucket': 2},
                                               'length': 10,'rules': {'absolute_expire_time': 172800},
                                               'snapshot': {'block_height': {'interval': 10}, 'path': '../data/wx-org1.chainmaker.org/tx_filter',
                                                             'serialize_interval': 10,'timed': {'interval': 10}, 'type': 0}},
                                               'sharding': {'birds_nest': {'cuckoo': {'bits_per_item': 11,'key_type': 1,
                                                                        'max_num_keys': 2000000,'table_type': 0,'tags_per_bucket': 2},
                                                             'length': 10,'rules': {'absolute_expire_time': 172800}},
                                               'length': 5,
                                               'snapshot': {'block_height': {'interval': 10},
                                                           'path': '../data/wx-org1.chainmaker.org/tx_filter',
                                                           'serialize_interval': 10,
                                                           'timed': {'interval': 10},
                                                           'type': 0},'timeout': 60},
                                               'type': 0}
        :param monitor: 节点monitor配置 eg. {'enabled': False, 'port': 14321}
        :param pprof: 节点pprof配置 eg. {'enabled': False, 'port': 24321}
        :param consensus: 共识扩展配置 eg. {'raft': {'snap_count': 10, 'async_wal_save': True, 'ticker': 1}
        :param scheduler: 节点调度器配置 eg {'rwset_log': False}
        :param storage: 节点存储配置 eg. {'bigfilter_config': {'fp_rate': 1e-09, 'redis_hosts_port': '127.0.0.1:6300,127.0.0.1:6301','redis_password': 'abcpass','tx_capacity': 1000000000},
                                         'blockdb_config': {'leveldb_config': {'store_path': '../data/wx-org1.chainmaker.org/block'},
                                                            'provider': 'leveldb'},
                                         'contract_eventdb_config': {'provider': 'sql',
                                                                     'sqldb_config': {'dsn': 'root:password@tcp(127.0.0.1:3306)/',
                                                                                      'sqldb_type': 'mysql'}},
                                         'disable_block_file_db': False,'disable_contract_eventdb': True,'enable_bigfilter': False,'enable_rwc': True,
                                         'historydb_config': {'disable_account_history': True, 'disable_contract_history': True,
                                                              'disable_key_history': False,
                                                              'leveldb_config': {'store_path': '../data/wx-org1.chainmaker.org/history'},
                                                              'provider': 'leveldb'},
                                         'logdb_segment_async': False,
                                         'logdb_segment_size': 128,
                                         'resultdb_config': {'leveldb_config': {'store_path': '../data/wx-org1.chainmaker.org/result'},
                                                             'provider': 'leveldb'},
                                         'rolling_window_cache_capacity': 55000,
                                         'state_cache_config': {'clean_window': 1000000000,'hard_max_cache_size': 1024,
                                                                'life_window': 3000000000000,'max_entry_size': 500},
                                         'statedb_config': {'leveldb_config': {'store_path': '../data/wx-org1.chainmaker.org/state'},
                                                            'provider': 'leveldb'},
                                         'store_path': '../data/wx-org1.chainmaker.org/ledgerData1',
                                         'unarchive_block_height': 300000,'write_block_type': 0}
        :param vm: 节点虚拟机配置 eg. {'go': {'contract_engine': {'host': '127.0.0.1', 'max_connection': 5, 'port': 22351},
                            'data_mount_path': '../data/wx-org1.chainmaker.org/go', 'dial_timeout': 10,'enable': False,
                            'log_in_console': False, 'log_level': 'INFO','log_mount_path': '../log/wx-org1.chainmaker.org/go',
                            'max_concurrency': 20,'max_recv_msg_size': 100,
                            'max_send_msg_size': 100,'protocol': 'tcp','runtime_server': {'port': 32351}}}
        :return:
        """
        if auth_type:
            self.chainmaker_config['auth_type'] = auth_type
        if log:
            self.chainmaker_config['log'].update(log)
        if crypto_engine:
            self.chainmaker_config['crypto_engine'] = crypto_engine
        if blockchain:
            self.chainmaker_config['blockchain'] = blockchain
        if node:
            self.chainmaker_config['node'].update(node)
        if net:
            self.chainmaker_config['net'].update(net)
        if txpool:
            self.chainmaker_config['txpool'].update(txpool)
        if rpc:
            self.chainmaker_config['rpc'].update(rpc)
        if tx_filter:
            self.chainmaker_config['tx_filter'].update(tx_filter)
        if monitor:
            self.chainmaker_config['monitor'].update(monitor)
        if pprof:
            self.chainmaker_config['pprof'].update(pprof)
        if consensus:
            self.chainmaker_config['consensus'].update(consensus)
        if scheduler:
            self.chainmaker_config['scheduler'].update(scheduler)
        if storage:
            self.chainmaker_config['storage'].update(storage)
        if vm:
            self.chainmaker_config['vm'].update(vm)

        if not self.host.exists(self._chainmaker_yml_bak_path):
            self.host.run(f'cp {self._chainmaker_yml_path} {self._chainmaker_yml_bak_path}')
        self.host.save_yaml(self.chainmaker_config, self._chainmaker_yml_path)
        self._cached_chainmaker_config = None

    def modify_log_level(self, origin_log_level: str = 'INFO', log_level: str = 'DEBUG'):
        if not self.host.exists(self._log_yml_bak_path):
            self.host.run(f'cp {self._log_yml_path} {self._log_yml_bak_path}')
        self.host.run(f'sed -i "s/{origin_log_level}/{log_level}/g" {self._log_yml_path}')

    def _clean(self):
        """清空节点数据及日志"""
        return self.host.run('rm -rf data/* ; rm -rf log/*', workspace=self._bin_path)

    def _kill(self) -> str:
        """
        杀掉节点进程
        :return: 命令行输出结果
        """
        logging.debug('杀死节点: %s' % self.name)
        return self.host.kill(self.pid)

    def _reset_config(self):
        """重置bc1.yml和chainmaker.yml配置"""
        if self.host.exists(self._bc1_yml_bak_path):
            self.host.run(f'rm -rf {self._bc1_yml_path}')
            self.host.run(f'mv {self._bc1_yml_bak_path} {self._bc1_yml_path}')
            self._cached_bc1_config = None

        if self.host.exists(self._chainmaker_yml_bak_path):
            self.host.run(f'rm -rf {self._chainmaker_yml_path}')
            self.host.run(f'mv {self._chainmaker_yml_bak_path} {self._chainmaker_yml_path}')
            self._cached_chainmaker_config = None

        if self.host.exists(self._log_yml_bak_path):
            self.host.run(f'rm -rf {self._log_yml_path}')
            self.host.run(f'mv {self._log_yml_bak_path} {self._log_yml_path}')

    @staticmethod
    def _guess_org_id_from_release_path(release_path: str):
        if 'node' in release_path:
            org_id, = (re.findall(r'node\d+', release_path) or ['public'])
        else:
            org_id, = (re.findall(r'wx-org\d+\.chainmaker\.org', release_path) or [''])
        return org_id


class ChainMakerCluster:
    """长安链服务器集群"""

    def __init__(self, nodes: List[ChainMakerNode]):
        self.nodes = nodes

    @property
    def active_node_cnt(self):
        """
        活动节点数量
        :return:
        """
        count = 0
        for node in self.nodes:
            if node.is_active:
                count += 1
        return count

    def start_nodes(self, nodes: List[str] = None):
        """
        启动多个节点
        :param nodes: 指定节点列表, eg. ['node1', 'node2']
        :return:
        """
        nodes = self._get_nodes(nodes)
        threads = []
        for node in nodes:
            threads.append(threading.Thread(target=node.start))
        [t.start() for t in threads]
        [t.join() for t in threads]
        for node in nodes:
            node.start()

    def stop_nodes(self, nodes: List[str] = None, clean: bool = False):
        """
        停止对多个节点
        :param nodes: 指定节点列表, eg. ['node1', 'node2']
        :param clean: 是否清理节点数据及日志
        :return:
        """
        nodes = self._get_nodes(nodes)
        threads = []
        for node in nodes:
            threads.append(threading.Thread(target=node.stop, args=(clean,)))
        [t.start() for t in threads]
        [t.join() for t in threads]

        for node in nodes:
            node.stop(clean)

    def restart_nodes(self, nodes: List[str] = None, clean: bool = False, duration: int = None,
                      reset_config: bool = False):
        """
        重启多个节点
        :param nodes: 指定节点列表, eg. ['node1', 'node2']
        :param clean: 是否清理节点数据及日志
        :param duration: 重启间隔时间
        :param reset_config: 是否重置对bc1.yml和chainmaker.yml的修改
        :return:
        """
        nodes = self._get_nodes(nodes)
        threads = []
        for node in nodes:
            threads.append(threading.Thread(target=node.restart, args=(clean, duration, reset_config)))
        [t.start() for t in threads]
        [t.join() for t in threads]
        for node in nodes:
            node.restart(clean, duration, reset_config)

    def reset(self):
        """重置集群"""
        self.restart_nodes(clean=True, reset_config=True)

    def modify_bc1_yml(self, chain_id: str = None, version: str = None, sequence: int = None, auth_type: str = None,
                       crypto: dict = None, contract: dict = None, vm: dict = None, block: dict = None,
                       core: dict = None,
                       account_config: dict = None, consensus: dict = None, trust_roots: List[dict] = None,
                       resource_policies: List[dict] = None, disabled_native_contract: List[str] = None,
                       nodes: List[str] = None, restart_nodes: bool = False):
        """
        修改节点bc1.yml配置
        :param chain_id: 链id eg. chain1
        :param version: 链版本 eg. v2.3.0
        :param sequence: 配置序号 eg. 0
        :param auth_type: 授权类型 eg. permissionedWithCert
        :param crypto: 加密配置 eg. {'hash': 'SHA256'}
        :param contract: 合约配置 eg. {'enable_sql_support': False}
        :param vm: 虚拟机配置 eg. {'addr_type': 2, support_list: ['wasmer', 'gasm', 'evm', 'dockergo', 'wxvm']}
        :param block: 区块配置 eg. {'tx_timestamp_verify': True, 'tx_timeout': 600, 'block_tx_capacity': 100,
                                  'block_size': 10, 'block_interval': 10}
        :param core: 核心配置 eg. {'tx_scheduler_timeout':10 , 'tx_scheduler_validate_timeout': 10,
                                 'enable_sender_group': False, 'enable_conflicts_bit_window': True}
        :param account_config: Gas账户配置 eg. {'enable_gas': False, 'gas_count': 0, 'default_gas': 0}
        :param consensus: 共识配置 eg. {'type': 3, 'nodes': [{'org_id': 'wx-org1.chainmaker.org',
                                                            'node_id': ['QmTTayzjbQqzzarWMo9HQSZsnZWLAQz2oefogKZuhbMnfD']}, ...],
                                       'ext_config': None}
        :param trust_roots: 信任组织根证书配置 eg. [{'org_id': 'wx-org1.chainmaker.org',
                                                  'root': ['../config/wx-org1.chainmaker.org/certs/ca/wx-org1.chainmaker.org/ca.crt']}]
        :param resource_policies: 权限配置 eg. [{'resource_name': 'CHAIN_CONFIG-NODE_ID_UPDATE',
                                                'policy': {'rule': 'SELF', org_list: None, role_list: ['admin']}, ...]
        :param disabled_native_contract: 禁用系统合约配置 eg. None
        """
        _nodes = self._get_nodes(nodes)
        for node_obj in _nodes:
            node_obj.modify_bc1_yml(chain_id, version, sequence, auth_type, crypto, contract, vm, block, core,
                                    account_config, consensus, trust_roots, resource_policies, disabled_native_contract)
        if restart_nodes:
            self.restart_nodes(nodes)

    def modify_chainmaker_yml(self, auth_type: str = None, log: dict = None, crypto_engine: str = None,
                              blockchain: List[dict] = None, node: dict = None, net: dict = None, txpool: dict = None,
                              rpc: dict = None, tx_filter: dict = None, monitor: dict = None, pprof: dict = None,
                              consensus: dict = None, scheduler: dict = None, storage: dict = None, vm: dict = None,
                              nodes: List[str] = None, restart_nodes: bool = False):
        """
        修改节点chainmaker.yml配置
        :param auth_type: 节点授权模式 eg. permissionedWithCert
        :param log: 节点日志配置 eg. {'config_file': '../config/wx-org1.chainmaker.org/log.yml'}
        :param crypto_engine: 节点国密引擎配置, 支持gmssl,tencentsm和tjfoc eg. tjfoc
        :param blockchain: 节点链配置 eg. [{'chainId: 'chain1', 'genesis': '../config/wx-org1.chainmaker.org/chainconfig/bc1.yml'}]
        :param node: 节点配置 eg. {'org_id': 'wx-org1.chainmaker.org', 'priv_key_file': '../config/wx-org1.chainmaker.org/certs/node/consensus1/consensus1.sign.key',
                                  'cert_file': '../config/wx-org1.chainmaker.org/certs/node/consensus1/consensus1.sign.crt',
                                  'cert_cache_size': 1000, 'cert_key_usage_check': True,
                                  'fast_sync': {'enabled: True, 'min_full_blocks': 10},
                                  'pkcs11': {'enabled': False, 'type': 'pkcs11', 'library': '/usr/local/lib64/pkcs11/libupkcs11.so',
                                             'label': 'HSM', 'password': '11111111', 'session_cache_size': 10, 'hash': 'SHA256'}}
        :param net: 节点网络配置 eg. {'provider': 'LibP2P','listen_addr': '/ip4/0.0.0.0/tcp/11301',
                                    'seeds': ['/ip4/127.0.0.1/tcp/11301/p2p/QmTTayzjbQqzzarWMo9HQSZsnZWLAQz2oefogKZuhbMnfD', ...],
                                    'tls': {'enabled': True, 'priv_key_file': '...', 'cert_file': '...', 'priv_enc_key_file': '...',
                                            'cert_enc_file': '...'}}
        :param txpool: 节点交易池配置 eg. {'pool_type': 'normal', 'max_txpool_size': 50000, 'max_config_txpool_size': 10,
                                         'is_dump_txs_in_queue': true, 'common_queue_num': 8, 'batch_max_size': 100,
                                         'batch_create_timeout': 50}
        :param rpc: 节点rpc配置 eg. {'blacklist': {'addresses': None},
                                    'check_chain_conf_trust_roots_change_interval': 60,
                                    'gateway': {'enabled': False, 'max_resp_body_size': 16},
                                    'max_recv_msg_size': 100,'max_send_msg_size': 100, 'port': 12301,'provider': 'grpc',
                                    'ratelimit': {'enabled': False,'token_bucket_size': -1,'token_per_second': -1,'type': 0},
                                    'subscriber': {'ratelimit': {'token_bucket_size': 100,'token_per_second': 100}},
                                    'tls': {'cert_enc_file': '../config/wx-org1.chainmaker.org/certs/node/consensus1/consensus1.tls.enc.crt',
                                            'cert_file': '../config/wx-org1.chainmaker.org/certs/node/consensus1/consensus1.tls.crt',
                                            'mode': 'twoway',
                                            'priv_enc_key_file': '../config/wx-org1.chainmaker.org/certs/node/consensus1/consensus1.tls.enc.key',
                                            'priv_key_file': '../config/wx-org1.chainmaker.org/certs/node/consensus1/consensus1.tls.key'}}
        :param tx_filter: 节点交易过滤器配置 eg. {'birds_nest': {'cuckoo': {'bits_per_item': 11, 'key_type': 1, 'max_num_keys': 2000000,'table_type': 0,'tags_per_bucket': 2},
                                               'length': 10,'rules': {'absolute_expire_time': 172800},
                                               'snapshot': {'block_height': {'interval': 10}, 'path': '../data/wx-org1.chainmaker.org/tx_filter',
                                                             'serialize_interval': 10,'timed': {'interval': 10}, 'type': 0}},
                                               'sharding': {'birds_nest': {'cuckoo': {'bits_per_item': 11,'key_type': 1,
                                                                        'max_num_keys': 2000000,'table_type': 0,'tags_per_bucket': 2},
                                                             'length': 10,'rules': {'absolute_expire_time': 172800}},
                                               'length': 5,
                                               'snapshot': {'block_height': {'interval': 10},
                                                           'path': '../data/wx-org1.chainmaker.org/tx_filter',
                                                           'serialize_interval': 10,
                                                           'timed': {'interval': 10},
                                                           'type': 0},'timeout': 60},
                                               'type': 0}
        :param monitor: 节点monitor配置 eg. {'enabled': False, 'port': 14321}
        :param pprof: 节点pprof配置 eg. {'enabled': False, 'port': 24321}
        :param consensus: 共识扩展配置 eg. {'raft': {'snap_count': 10, 'async_wal_save': True, 'ticker': 1}
        :param scheduler: 节点调度器配置 eg {'rwset_log': False}
        :param storage: 节点存储配置 eg. {'bigfilter_config': {'fp_rate': 1e-09, 'redis_hosts_port': '127.0.0.1:6300,127.0.0.1:6301','redis_password': 'abcpass','tx_capacity': 1000000000},
                                         'blockdb_config': {'leveldb_config': {'store_path': '../data/wx-org1.chainmaker.org/block'},
                                                            'provider': 'leveldb'},
                                         'contract_eventdb_config': {'provider': 'sql',
                                                                     'sqldb_config': {'dsn': 'root:password@tcp(127.0.0.1:3306)/',
                                                                                      'sqldb_type': 'mysql'}},
                                         'disable_block_file_db': False,'disable_contract_eventdb': True,'enable_bigfilter': False,'enable_rwc': True,
                                         'historydb_config': {'disable_account_history': True, 'disable_contract_history': True,
                                                              'disable_key_history': False,
                                                              'leveldb_config': {'store_path': '../data/wx-org1.chainmaker.org/history'},
                                                              'provider': 'leveldb'},
                                         'logdb_segment_async': False,
                                         'logdb_segment_size': 128,
                                         'resultdb_config': {'leveldb_config': {'store_path': '../data/wx-org1.chainmaker.org/result'},
                                                             'provider': 'leveldb'},
                                         'rolling_window_cache_capacity': 55000,
                                         'state_cache_config': {'clean_window': 1000000000,'hard_max_cache_size': 1024,
                                                                'life_window': 3000000000000,'max_entry_size': 500},
                                         'statedb_config': {'leveldb_config': {'store_path': '../data/wx-org1.chainmaker.org/state'},
                                                            'provider': 'leveldb'},
                                         'store_path': '../data/wx-org1.chainmaker.org/ledgerData1',
                                         'unarchive_block_height': 300000,'write_block_type': 0}
        :param vm: 节点虚拟机配置 eg. {'go': {'contract_engine': {'host': '127.0.0.1', 'max_connection': 5, 'port': 22351},
                            'data_mount_path': '../data/wx-org1.chainmaker.org/go', 'dial_timeout': 10,'enable': False,
                            'log_in_console': False, 'log_level': 'INFO','log_mount_path': '../log/wx-org1.chainmaker.org/go',
                            'max_concurrency': 20,'max_recv_msg_size': 100,
                            'max_send_msg_size': 100,'protocol': 'tcp','runtime_server': {'port': 32351}}}
        :return:
        """
        _nodes = self._get_nodes(nodes)
        for node_obj in _nodes:
            node_obj.modify_chainmaker_yml(auth_type, log, crypto_engine, blockchain, node, net, txpool, rpc, tx_filter,
                                           monitor, pprof, consensus, scheduler, storage, vm)
        if restart_nodes:
            self.restart_nodes(nodes)

    def modify_log_level(self, origin_log_level: str='INFO', log_level: str='DEBUG', nodes: List[str]=None,
                         restart_nodes: bool = False):
        _nodes = self._get_nodes(nodes)
        for node in _nodes:
            node.modify_log_level(origin_log_level, log_level)

        if restart_nodes:
            self.restart_nodes(nodes)

    def enable_sql_support(self, dns='root:password@tcp(127.0.0.1:3306)/'):
        """修改所有节点bc1.yml及chainmaker.yml配置"""
        self.modify_bc1_yml(contract={'enable_sql_support': True})
        for node in self.nodes:
            node.modify_chainmaker_yml(
                storage={'db_prefix': f'org{node.index + 1}_',
                         'statedb_config': {'provider': 'sql', 'sqldb_config': {'sqldb_type': 'mysql', 'dns': dns}}})
        self.restart_nodes(clean=True)

    def enable_archive_block(self, unarchive_block_height: int=10):
        """启动归档区块(需要disable_block_file_db并清数据重启)"""
        self.modify_chainmaker_yml(storage={'unarchive_block_height': unarchive_block_height,
                                            'disable_block_file_db': True})
        self.restart_nodes(clean=True)

    def enable_vm_docker_go(self):  # todo
        for node in self.nodes:
            if 'docker-go' not in node.chainmaker_config['vm']:
                node.modify_chainmaker_yml(vm={'docker_go': {'docker_vm_host': '127.0.0.1',
                                                             'docker_vm_port': 22451 + node.index,
                                                             'dockervm_log_path': f'../log/{node.org_id}/docker-go',
                                                             'dockervm_mount_path': f'../data/{node.org_id}/docker-go',
                                                             'enable_dockervm': True,
                                                             'log_in_console': True,
                                                             'log_level': 'DEBUG',
                                                             'max_connection': 5,
                                                             'max_recv_msg_size': 20,
                                                             'max_send_msg_size': 20,
                                                             'uds_open': True}})

    # def modify_txpool_config(self, pool_type: str = None, max_txpool_size: int = None,
    #                          max_config_txpool_size: int = None,
    #                          is_dump_txs_in_queue: bool = True, common_queue_num: int = None,
    #                          batch_max_size: int = None,
    #                          batch_create_timeout: int = None):
    #     """
    #     修改所有节点chainmaker.yml交易池配置
    #     原配置: {'pool_type': 'normal', 'max_txpool_size': 50000, 'max_config_txpool_size': 10,
    #             'is_dump_txs_in_queue': True, 'common_queue_num': 8, 'batch_max_size': 100,
    #             'batch_create_timeout': 50}
    #     """
    #     txpool_config = {}
    #     if pool_type is not None:
    #         txpool_config['pool_type'] = pool_type
    #     if max_txpool_size is not None:
    #         txpool_config['max_txpool_size'] = max_txpool_size
    #     if max_config_txpool_size is not None:
    #         txpool_config['max_config_txpool_size'] = max_config_txpool_size
    #     if is_dump_txs_in_queue is not None:
    #         txpool_config['is_dump_txs_in_queue'] = is_dump_txs_in_queue
    #     if common_queue_num is not None:
    #         txpool_config['common_queue_num'] = common_queue_num
    #     if batch_max_size is not None:
    #         txpool_config['batch_max_size'] = batch_max_size
    #     if batch_create_timeout is not None:
    #         txpool_config['batch_create_timeout'] = batch_create_timeout
    #     self.modify_chainmaker_yml(txpool=txpool_config)

    def _get_node(self, node: str) -> ChainMakerNode:
        """
        根据节点名称获取节点对象
        :param node: 节点名称 eg. node1
        :return: 节点名称对应的节点对象
        """
        index = int(node.lstrip('node')) - 1
        return self.nodes[index]

    def _get_nodes(self, nodes: List[str]):
        return [self._get_node(node) for node in nodes] if nodes else self.nodes

    @staticmethod
    def _get_release_paths_by_chainmaker_go_path(host: Host, chainmaker_go_path: str):
        """从标准chainmaker-go/build/release目录得到有序的节点release路径列表"""
        build_release_path = f'{chainmaker_go_path}/build/release'
        result = host.run('ls -d */', workspace=build_release_path).split()
        if 'node' in result[0]:
            release_dirs = sorted(result, key=lambda x: int(x.split('-')[2].lstrip('node').rstrip('/')))
        else:
            release_dirs = sorted(result, key=lambda x: int(x.split('-')[3].lstrip('org').rstrip('.chainmaker.org/')))
        release_paths = [f'{build_release_path}/{item}' for item in release_dirs]
        return release_paths

    @classmethod
    def from_conf(cls, server_config: dict):
        """
        根据配置生成长安链集群对象
        :param server_config:
            eg1. 单主机标准chainmaker-go节点配置(节点统一位于chainmaker-go/build/release下){
                {'host': {'host': '127.0.0.1', 'port': 36000, 'user': 'root', 'password': '...'},
                'chainmaker_go_path': '/home/hzc/chainmaker-go',
                'rpc_start_port': 12301
                }
            eg2. 单主机分布式节点配置
                {'host': {'host': '127.0.0.1', 'port': 36000, 'user': 'root', 'password': '...'},
                'rpc_start_port': 12301,
                'nodes': [
                    {'release_path': '/home/hzc/chainmaker-go/build/release/chainmaker-v3.0.0_alpha-wx-org1.chainmaker.org'},
                    {'release_path': '/home/hzc/chainmaker-go/build/release/chainmaker-v3.0.0_alpha-wx-org2.chainmaker.org'},
                    {'release_path': '/home/hzc/chainmaker-go/build/release/chainmaker-v3.0.0_alpha-wx-org3.chainmaker.org'},
                    {'release_path': '/home/hzc/chainmaker-go/build/release/chainmaker-v3.0.0_alpha-wx-org4.chainmaker.org',
                     'rpc_port': 12304},
                    ]
                }
            eg3. 多主机节点配置
                {'nodes': [
                    {'host': {'host': '127.0.0.1', 'port': 36000, 'user': 'root', 'password': '...')},
                     'release_path': '/home/hzc/chainmaker-go/build/release/chainmaker-v3.0.0_alpha-wx-org1.chainmaker.org'},
                    {'host': {'host': '127.0.0.2', 'port': 36000, 'user': 'root', 'password': '...')},
                     'release_path': '/home/hzc/chainmaker-go/build/release/chainmaker-v3.0.0_alpha-wx-org2.chainmaker.org'},
                    {'host': {'host': '127.0.0.3', 'port': 36000, 'user': 'root', 'password': '...')},
                     'release_path': '/home/hzc/chainmaker-go/build/release/chainmaker-v3.0.0_alpha-wx-org3.chainmaker.org'},
                    {'host': {'host': '127.0.0.4', 'port': 36000, 'user': 'root', 'password': '...')},
                     'release_path': '/home/hzc/chainmaker-go/build/release/chainmaker-v3.0.0_alpha-wx-org4.chainmaker.org',
                     'rpc_port': 12304},
                    ]
                }
        :return: 长安链集群对象
        """
        host_config = server_config.get('host')
        host = Host(**host_config) if host_config else None
        rpc_start_port = server_config.get('rpc_start_port') or 12301

        if 'nodes' in server_config:
            nodes_config = server_config.get('nodes')
        else:
            assert host_config, 'server_config需包含host配置'
            chainmaker_go_path = server_config.get('chainmaker_go_path') or f"{host.workspace}/chainmaker-go"
            release_paths = cls._get_release_paths_by_chainmaker_go_path(host, chainmaker_go_path)
            nodes_config = [{'release_path': item} for item in release_paths]

        nodes = []
        for index, item in enumerate(nodes_config):
            node_host = host if host_config else Host(**item.get('host'))
            release_path = item.get('release_path')
            rpc_port = item.get('rpc_port') or rpc_start_port + index
            node = ChainMakerNode(index=index, host=node_host, release_path=release_path, rpc_port=rpc_port)
            nodes.append(node)
        return cls(nodes=nodes)
