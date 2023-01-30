import os
import sys
# noinspection PyPackageRequirements
import json

cur_file_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = f'{cur_file_dir}/../fabrique_nodes_core'
sys.path.append(lib_dir)
os.chdir(cur_file_dir)

import tests.import_spoofer  # noqa: F401

import fabrique_nodes_core.configs_model as cm
from fabrique_nodes_core.convertors import convert_node_data_to_config


def file2str(pth):
    with open(pth) as fp:
        txt = fp.read()
    return txt


actor_data = json.loads(file2str(f'{cur_file_dir}/data/project.json'))


def cfg2model(cfg_dict):
    cfg = cm.PipelineModel(**cfg_dict)
    cfg_data = {k: v.data for k, v in cfg.__dict__['nodes'].items()}

    def check_edges(edges_iter, nodes):
        for edge in edges_iter:
            source_node_id = edge.source
            source_port_id = edge.sourceHandle
            target_node_id = edge.target
            target_port_id = edge.targetHandle
            source_node = nodes[source_node_id]
            source_config = convert_node_data_to_config(source_node.data)
            target_node = nodes[target_node_id]
            target_config = convert_node_data_to_config(target_node.data)
            
            ports_in_ids = [port.id_ for port in target_config.ports_in]
            ports_out_ids = [port.id_ for port in source_config.ports_out]

            assert source_port_id in ports_out_ids
            assert target_port_id in ports_in_ids

    check_edges(cfg.edges.values(), cfg.nodes)
    
    for actor in cfg.actors.values():
        check_edges(actor.edges.values(), actor.nodes)

    # outputs = {int(k): {key: val.connections for key, val in v.outputs.items()} for k, v in cfg.nodes.items()}
    # inputs = {int(k): {key: val.connections for key, val in v.inputs.items()} for k, v in cfg.nodes.items()}
    cfg_data = {k: v.data for k, v in cfg.__dict__['nodes'].items()}
    return cfg, cfg_data


def test_cfg_model():
    _, cfg_data = cfg2model(actor_data)
    # assert len(outputs) == 5
    # assert len(inputs) == 5
    assert len(cfg_data) == 5
