#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) THL A29 Limited, a Tencent company. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0
#
# @FileName     :   deploy_utils.py
# @Function     :   chainmaker-go部署实用方法
import os
import time
from typing import List

try:
    from hostz import Host, Local
except ImportError:
    print('please install hostz: pip install hostz')

from chainmaker.keys import AuthType, ConsensusType, HashType

CHAINMAKER_GO_REPO = 'git@git.code.tencent.com:ChainMaker/chainmaker-go.git'
CHAINMAKER_CRYPTOGEN_REPO = 'git@git.code.tencent.com:ChainMaker/chainmaker-cryptogen.git'
VM_ENGINE_REPO = 'git@git.code.tencent.com:ChainMaker/vm-engine.git'
VM_DOCKER_GO_REPO = 'git@git.code.tencent.com:ChainMaker/vm-docker-go.git'


class SingleHostChainBuild:
    def __init__(self, host: Host):
        self.host = host
        self.workspace = self.host.workspace.rstrip("/")
        self.chainmaker_go_path = f'{self.workspace}/chainmaker-go'
        self.chainmaker_cryptogen_path = f'{self.workspace}/chainmaker-cryptogen'
        self.vm_engine_path = f'{self.workspace}/vm-engine'

        self.scripts_path = f'{self.chainmaker_go_path}/scripts'

    @staticmethod
    def _get_prepare_script_by_auth_type(auth_type: AuthType):
        if auth_type == AuthType.PermissionedWithCert:
            prepare_script = 'prepare.sh'
        elif auth_type == AuthType.PermissionedWithKey:
            prepare_script = 'prepare_pwk.sh'
        else:
            prepare_script = 'prepare_pk.sh'
        return prepare_script

    def update(self, branch, enable_vm_go: bool = False, enable_vm_docker_go: bool = False):
        self._prepare_chainmaker_cryptogen(branch)
        self._prepare_chainmaker_go(branch)
        if enable_vm_go:
            self._prepare_vm_engine(branch)
        if enable_vm_docker_go:
            self._prepare_vm_docker_go(branch)

        print(f'重置并切换chainmaker-go分支为{branch}')
        self.host.run(f'git reset --hard && git checkout {branch} && git pull;', workspace=self.chainmaker_go_path)
        return self

    def prepare(self, auth_type=AuthType.PermissionedWithCert,
                chain_cnt: int = 1, node_cnt: int = 4, hash_type: HashType = HashType.SHA256,
                consensus_type: ConsensusType = ConsensusType.TBFT,
                p2p_port: int = 11301, rpc_port: int = 12301,
                vm_go_runtime_port: int = 32351, vm_go_engine_port: int = 22351,
                vm_go_transport_protocol='tcp', log_level: str = 'INFO',
                enable_vm_go: bool = False):
        # version = branch.split('_')[0]
        # vm_engine_branch = f'{version}_qc'

        enable_vm_go = 'true' if enable_vm_go else 'false'
        prepare_script = self._get_prepare_script_by_auth_type(auth_type)

        # if enable_vm_go is True:
        # self._prepare_vm_engine(vm_engine_branch)

        self.stop_cluster()

        print(f'执行{prepare_script}')
        if auth_type == AuthType.PermissionedWithCert:
            cmd = (f'sh prepare.sh {node_cnt} {chain_cnt} {p2p_port} {rpc_port} '
                   f'{vm_go_runtime_port} {vm_go_engine_port} '
                   f'-c {consensus_type.value} -l {log_level} '
                   f'-v {enable_vm_go} --vtp={vm_go_transport_protocol} --vlog={log_level};')

        elif auth_type == AuthType.Public:
            cmd = (f'sh prepare_pk.sh {node_cnt} {chain_cnt} {p2p_port} {rpc_port} '
                   f'{vm_go_runtime_port} {vm_go_engine_port} '
                   f'-c {consensus_type.value} -l {log_level} '
                   f'--hash {hash_type.name} '
                   f'-v {enable_vm_go} --vtp={vm_go_transport_protocol} --vlog={log_level}')
        else:
            cmd = (f'sh prepare_pwk.sh {node_cnt} {chain_cnt} {p2p_port} {rpc_port} '
                   f'{vm_go_runtime_port} {vm_go_engine_port} '
                   f'-c {consensus_type.value} -l {log_level} --hash {hash_type.name} '
                   f'-v {enable_vm_go} --vtp={vm_go_transport_protocol} --vlog={log_level}')
        self.host.run(cmd, workspace=self.scripts_path)
        return self

    def build_release(self):
        print('执行build_release.sh')
        self.host.run(f'sh build_release.sh;', workspace=self.scripts_path)
        return self

    def start_cluster(self):
        print('启动集群')
        self.host.run(f'sh cluster_quick_start.sh normal;', workspace=self.scripts_path)
        self.wait(1)
        return self

    def stop_cluster(self, clean: bool = True):
        print('停止集群')
        cmd = 'sh cluster_quick_stop.sh clean;' if clean else 'sh cluster_quick_stop.sh;'
        self.host.run(cmd, workspace=self.scripts_path)
        self.wait(1)
        return self

    @staticmethod
    def wait(self, secs: int = 1):
        time.sleep(secs)
        return self

    def modify_chainmaker_cryptogen_config(self, auth_type, pk_algo: str, hash_algo: str):
        if auth_type == AuthType.PermissionedWithCert:
            config_file = f'{self.chainmaker_cryptogen_path}/config/crypto_config_template.yml'
        elif auth_type == AuthType.PermissionedWithKey:
            config_file = f'{self.chainmaker_cryptogen_path}/config/pwk_config_template.yml'
        else:
            config_file = f'{self.chainmaker_cryptogen_path}/config/pk_config_template.yml'

        self.host.execute(f"sed -i 's/pk_algo: .*/pk_algo: {pk_algo}/g' {config_file}")

        if auth_type == AuthType.PermissionedWithCert:
            self.host.execute(f"sed -i 's/ski_hash: .*/ski_hash: {hash_algo}/g' {config_file}")
        else:
            self.host.execute(f"sed -i 's/hash_algo: .*/hash_algo: {hash_algo}/g' {config_file}")
        return self

    def deploy(self, branch: str, auth_type=AuthType.PermissionedWithCert,
               chain_cnt: int = 1, node_cnt: int = 10, consensus_node_cnt: int = 4,
               consensus_type: ConsensusType = ConsensusType.TBFT,
               p2p_port: int = 11301, rpc_port: int = 12301,
               vm_go_runtime_port: int = 32351, vm_go_engine_port: int = 22351,
               vm_go_transport_protocol='tcp',
               log_level: str = 'INFO',
               enable_vm_go: bool = False, enable_vm_docker_go: bool = False):
        pass

    # print('修改为4个共识节点')
    # self.host.run("sed -i '143,148d' ../build/config/node*/chainmaker.yml && "
    #               "sed -i '141,158d' ../build/config/node*/chainconfig/bc1.yml &&"
    #               "sed -i '171,188d' ../build/config/node*/chainconfig/bc1.yml", workspace=scripts_path)

    # print(f'扩展crypto-config到10节点')
    # self._extend_crypto_config(count=10, auth_type=auth_type, workspace=workspace)

    # print('停止节点5-10')
    # self.stop_nodes(['node5', 'node6', 'node7', 'node8', 'node9', 'node10'])

    def check(self):
        print('检查chainmaker节点数')
        result = self.host.run('ps -ef | grep "./chainmaker start -c" | grep -v "grep" | wc -l')
        return result

    def _prepare_chainmaker_go(self, branch: str):
        if not self.host.exists(self.chainmaker_go_path):
            self.host.run(f'git clone -b {branch} {CHAINMAKER_GO_REPO}')
        if not self.host.exists(f'{self.chainmaker_go_path}/tools/chainmaker-cryptogen'):
            self.host.run(f'ln -s {self.chainmaker_cryptogen_path} {self.chainmaker_go_path}/tools/')

    def _prepare_chainmaker_cryptogen(self, branch: str):
        chainmaker_cryptogen_path = f'{self.workspace}/chainmaker-cryptogen'
        if not self.host.exists(chainmaker_cryptogen_path):
            self.host.run(f'git clone -b {branch} {CHAINMAKER_CRYPTOGEN_REPO}', workspace=self.workspace)
            self.host.run('make')

    def _prepare_vm_engine(self, branch: str):
        version = branch.split('_')[0]
        vm_engine_path = f'{self.workspace}/vm-engine'
        if not self.host.exists(vm_engine_path):
            self.host.run(f'git clone -b {branch} {VM_ENGINE_REPO}', workspace=self.workspace)
        print('检查docker镜像')
        result = self.host.run(f'docker images | grep "chainmaker-vm-engine" | grep "{version}"')
        if not result:
            self.host.run(f'git reset --hard && git checkout {branch} && make build-image',
                          workspace=vm_engine_path)

    def _prepare_vm_docker_go(self, branch: str):
        version = branch.split('_')[0]
        vm_docker_go_path = f'{self.workspace}/vm-docker-go'
        if not self.host.exists(vm_docker_go_path):
            self.host.run(f'git clone -b {branch} {VM_DOCKER_GO_REPO}', workspace=self.workspace)
        print('检查docker镜像')
        result = self.host.run(f'docker images | grep "chainmaker-vm-docker-go" | grep "{version}"')
        if not result:
            self.host.run(f'git reset --hard && git checkout {branch} && make build-image',
                          workspace=vm_docker_go_path)

    def _enable_vm_docker_go_in_chainmaker_yml(self):
        chainmaker_yml_vm_docker_go_config = '''# Docker go virtual machine configuration
      docker_go:
        # Enable docker go virtual machine
        enable_dockervm: true
        # Mount point in chainmaker
        dockervm_mount_path: ../data/wx-org1.chainmaker.org/docker-go
        # Specify log file path
        dockervm_log_path: ../log/wx-org1.chainmaker.org/docker-go
        # Whether to print log at terminal
        log_in_console: true
        # Log level
        log_level: DEBUG
        # Unix domain socket open, used for chainmaker and docker manager communication
        uds_open: true
        # docker vm contract service host, default 127.0.0.1
        docker_vm_host: 127.0.0.1
        # docker vm contract service port, default 22351
        docker_vm_port: 22451
        # Grpc max send message size, Default size is 4, Unit: MB
        max_send_msg_size: 20
        # Grpc max receive message size, Default size is 4, Unit: MB
        max_recv_msg_size: 20
        # max number of connection created to connect docker vm service
        max_connection: 5'''
        chainmaker_go_path = f'{self.workspace}/chainmaker-go'
        any_chainmaker_yml_path = f'{chainmaker_go_path}/build/release/${{release_path}}/config/*/chainmaker.yml'
        self.host.run(f"for release_path in `ls -d */` ; do echo '{chainmaker_yml_vm_docker_go_config}' "
                      f">> {any_chainmaker_yml_path}; done",
                      workspace=f'{self.workspace}/chainmaker-go/build/release')

    def distribute(self, nodes_config: List[dict]):
        # 拷贝release包到各节点
        result = self.host.run('ls -rt| grep "chainmaker" | grep ".gz";',
                               workspace=f'{self.chainmaker_go_path}/build/release/').split()

        if 'node1' in result[0]:
            result = sorted(result, key=lambda x: int(x.split('-')[2].lstrip('node').rstrip('/')))
        else:
            result = sorted(result, key=lambda x: int(x.split('-')[3].lstrip('org').rstrip('.chainmaker.org/')))

        for _from, node_config in zip(result, nodes_config):
            file_name = os.path.basename(_from)
            host, port, user, password = (node_config['host'], node_config.get('port'), node_config.get('user'),
                                          node_config['password'])
            _to = f"{node_config.get('workspace')}/{file_name}"
            # self.host.scp(_from, _to, host, user, password, port, workspace=f'{self.chainmaker_go_path}/build/release/')
            node_host = Host(host, port, user, password, workspace=os.path.dirname(_to))
            node_host.untar(_to)
            node_host.run(f'rm -rf {_to}')



class MultiSignChainBuilder:
    def __init__(self, workspace):
        self.host = Local(workspace=workspace)

    def build_release(self):
        pass

    def deploy(self, nodes_config: List[dict], slave_config: dict):
        """分发"""
        # 拷贝release包到各节点
        result = self.host.run('ls -rt| grep "chainmaker" | grep ".gz";',
                               workspace=f'{self.chainmaker_go_path}/build/release/').split()

        if 'node1' in result[0]:
            result = sorted(result, key=lambda x: int(x.split('-')[2].lstrip('node').rstrip('/')))
        else:
            result = sorted(result, key=lambda x: int(x.split('-')[3].lstrip('org').rstrip('.chainmaker.org/')))

        for _from, node_config in zip(result, nodes_config):
            user = node_config.get('user')
            password = node_config.get('password')
            port = node_config.get('port')
            _to = node_config.get('workspace')
            self.host.scp(_from, _to, user, password, port)

        # 拷贝crypto-config到压测机
        _from = self.host.run('ls -rt| grep "crypto-config" | grep ".gz";',
                              workspace=f'{self.chainmaker_go_path}/build/release/').split()
        user = slave_config.get('user')
        password = slave_config.get('password')
        port = slave_config.get('port')
        _to = slave_config.get('workspace')
        self.host.scp(_from, _to, user, password, port)


class DockerChainBuild:
    pass


class K8sChainBuild:
    pass
