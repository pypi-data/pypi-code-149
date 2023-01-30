# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow_gnn/proto/graph_schema.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow.core.example import feature_pb2 as tensorflow_dot_core_dot_example_dot_feature__pb2
from tensorflow.core.framework import tensor_shape_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2
from tensorflow.core.framework import types_pb2 as tensorflow_dot_core_dot_framework_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow_gnn/proto/graph_schema.proto',
  package='tensorflow_gnn',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\'tensorflow_gnn/proto/graph_schema.proto\x12\x0etensorflow_gnn\x1a%tensorflow/core/example/feature.proto\x1a,tensorflow/core/framework/tensor_shape.proto\x1a%tensorflow/core/framework/types.proto\"\xf1\x02\n\x0bGraphSchema\x12(\n\x07\x63ontext\x18\x01 \x01(\x0b\x32\x17.tensorflow_gnn.Context\x12<\n\tnode_sets\x18\x02 \x03(\x0b\x32).tensorflow_gnn.GraphSchema.NodeSetsEntry\x12<\n\tedge_sets\x18\x03 \x03(\x0b\x32).tensorflow_gnn.GraphSchema.EdgeSetsEntry\x12(\n\x04info\x18\x04 \x01(\x0b\x32\x1a.tensorflow_gnn.OriginInfo\x1aH\n\rNodeSetsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.tensorflow_gnn.NodeSet:\x02\x38\x01\x1aH\n\rEdgeSetsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.tensorflow_gnn.EdgeSet:\x02\x38\x01\"\xe9\x01\n\x07\x46\x65\x61ture\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12#\n\x05\x64type\x18\x02 \x01(\x0e\x32\x14.tensorflow.DataType\x12+\n\x05shape\x18\x03 \x01(\x0b\x32\x1c.tensorflow.TensorShapeProto\x12\x0e\n\x06source\x18\x04 \x01(\t\x12*\n\rsample_values\x18\x06 \x01(\x0b\x32\x13.tensorflow.Feature\x12/\n\x0e\x65xample_values\x18\x05 \x03(\x0b\x32\x13.tensorflow.FeatureB\x02\x18\x01*\n\x08\x80\x80\x04\x10\x80\x80\x80\x80\x02\"\xb3\x02\n\x08\x42igQuery\x12\x38\n\ntable_spec\x18\x01 \x01(\x0b\x32\".tensorflow_gnn.BigQuery.TableSpecH\x00\x12\r\n\x03sql\x18\x02 \x01(\tH\x00\x12@\n\x0bread_method\x18\x03 \x01(\x0e\x32#.tensorflow_gnn.BigQuery.ReadMethod:\x06\x45XPORT\x12\x18\n\treshuffle\x18\x04 \x01(\x08:\x05\x66\x61lse\x1a<\n\tTableSpec\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x61taset\x18\x02 \x01(\t\x12\r\n\x05table\x18\x03 \x01(\t\":\n\nReadMethod\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\n\n\x06\x45XPORT\x10\x01\x12\x0f\n\x0b\x44IRECT_READ\x10\x02\x42\x08\n\x06source\"\xb7\x01\n\x08Metadata\x12\x30\n\x05\x65xtra\x18\x01 \x03(\x0b\x32!.tensorflow_gnn.Metadata.KeyValue\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\x12\x13\n\x0b\x63\x61rdinality\x18\x03 \x01(\x03\x12*\n\x08\x62igquery\x18\x04 \x01(\x0b\x32\x18.tensorflow_gnn.BigQuery\x1a&\n\x08KeyValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\xb8\x01\n\x07\x43ontext\x12\x37\n\x08\x66\x65\x61tures\x18\x01 \x03(\x0b\x32%.tensorflow_gnn.Context.FeaturesEntry\x12*\n\x08metadata\x18\x02 \x01(\x0b\x32\x18.tensorflow_gnn.Metadata\x1aH\n\rFeaturesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.tensorflow_gnn.Feature:\x02\x38\x01\"\xde\x01\n\x07NodeSet\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x37\n\x08\x66\x65\x61tures\x18\x02 \x03(\x0b\x32%.tensorflow_gnn.NodeSet.FeaturesEntry\x12\x0f\n\x07\x63ontext\x18\x03 \x03(\t\x12*\n\x08metadata\x18\x04 \x01(\x0b\x32\x18.tensorflow_gnn.Metadata\x1aH\n\rFeaturesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.tensorflow_gnn.Feature:\x02\x38\x01\"\xfe\x01\n\x07\x45\x64geSet\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x37\n\x08\x66\x65\x61tures\x18\x02 \x03(\x0b\x32%.tensorflow_gnn.EdgeSet.FeaturesEntry\x12\x0e\n\x06source\x18\x03 \x01(\t\x12\x0e\n\x06target\x18\x04 \x01(\t\x12\x0f\n\x07\x63ontext\x18\x05 \x03(\t\x12*\n\x08metadata\x18\x06 \x01(\x0b\x32\x18.tensorflow_gnn.Metadata\x1aH\n\rFeaturesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.tensorflow_gnn.Feature:\x02\x38\x01\"M\n\nOriginInfo\x12-\n\ngraph_type\x18\x01 \x01(\x0e\x32\x19.tensorflow_gnn.GraphType\x12\x10\n\x08root_set\x18\x02 \x03(\t*=\n\x07SetType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07\x43ONTEXT\x10\x01\x12\t\n\x05NODES\x10\x02\x12\t\n\x05\x45\x44GES\x10\x03*D\n\tGraphType\x12\r\n\tUNDEFINED\x10\x00\x12\x08\n\x04\x46ULL\x10\x01\x12\x0c\n\x08SUBGRAPH\x10\x02\x12\x10\n\x0cRANDOM_WALKS\x10\x03')
  ,
  dependencies=[tensorflow_dot_core_dot_example_dot_feature__pb2.DESCRIPTOR,tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2.DESCRIPTOR,tensorflow_dot_core_dot_framework_dot_types__pb2.DESCRIPTOR,])

_SETTYPE = _descriptor.EnumDescriptor(
  name='SetType',
  full_name='tensorflow_gnn.SetType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTEXT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NODES', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EDGES', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2035,
  serialized_end=2096,
)
_sym_db.RegisterEnumDescriptor(_SETTYPE)

SetType = enum_type_wrapper.EnumTypeWrapper(_SETTYPE)
_GRAPHTYPE = _descriptor.EnumDescriptor(
  name='GraphType',
  full_name='tensorflow_gnn.GraphType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FULL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBGRAPH', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RANDOM_WALKS', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2098,
  serialized_end=2166,
)
_sym_db.RegisterEnumDescriptor(_GRAPHTYPE)

GraphType = enum_type_wrapper.EnumTypeWrapper(_GRAPHTYPE)
UNSPECIFIED = 0
CONTEXT = 1
NODES = 2
EDGES = 3
UNDEFINED = 0
FULL = 1
SUBGRAPH = 2
RANDOM_WALKS = 3


_BIGQUERY_READMETHOD = _descriptor.EnumDescriptor(
  name='ReadMethod',
  full_name='tensorflow_gnn.BigQuery.ReadMethod',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPORT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIRECT_READ', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1031,
  serialized_end=1089,
)
_sym_db.RegisterEnumDescriptor(_BIGQUERY_READMETHOD)


_GRAPHSCHEMA_NODESETSENTRY = _descriptor.Descriptor(
  name='NodeSetsEntry',
  full_name='tensorflow_gnn.GraphSchema.NodeSetsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow_gnn.GraphSchema.NodeSetsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow_gnn.GraphSchema.NodeSetsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=407,
  serialized_end=479,
)

_GRAPHSCHEMA_EDGESETSENTRY = _descriptor.Descriptor(
  name='EdgeSetsEntry',
  full_name='tensorflow_gnn.GraphSchema.EdgeSetsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow_gnn.GraphSchema.EdgeSetsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow_gnn.GraphSchema.EdgeSetsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=481,
  serialized_end=553,
)

_GRAPHSCHEMA = _descriptor.Descriptor(
  name='GraphSchema',
  full_name='tensorflow_gnn.GraphSchema',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='context', full_name='tensorflow_gnn.GraphSchema.context', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_sets', full_name='tensorflow_gnn.GraphSchema.node_sets', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='edge_sets', full_name='tensorflow_gnn.GraphSchema.edge_sets', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='tensorflow_gnn.GraphSchema.info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GRAPHSCHEMA_NODESETSENTRY, _GRAPHSCHEMA_EDGESETSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=184,
  serialized_end=553,
)


_FEATURE = _descriptor.Descriptor(
  name='Feature',
  full_name='tensorflow_gnn.Feature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='tensorflow_gnn.Feature.description', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dtype', full_name='tensorflow_gnn.Feature.dtype', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shape', full_name='tensorflow_gnn.Feature.shape', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='tensorflow_gnn.Feature.source', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sample_values', full_name='tensorflow_gnn.Feature.sample_values', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='example_values', full_name='tensorflow_gnn.Feature.example_values', index=5,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(65536, 536870912), ],
  oneofs=[
  ],
  serialized_start=556,
  serialized_end=789,
)


_BIGQUERY_TABLESPEC = _descriptor.Descriptor(
  name='TableSpec',
  full_name='tensorflow_gnn.BigQuery.TableSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project', full_name='tensorflow_gnn.BigQuery.TableSpec.project', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataset', full_name='tensorflow_gnn.BigQuery.TableSpec.dataset', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='table', full_name='tensorflow_gnn.BigQuery.TableSpec.table', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=969,
  serialized_end=1029,
)

_BIGQUERY = _descriptor.Descriptor(
  name='BigQuery',
  full_name='tensorflow_gnn.BigQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_spec', full_name='tensorflow_gnn.BigQuery.table_spec', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sql', full_name='tensorflow_gnn.BigQuery.sql', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='read_method', full_name='tensorflow_gnn.BigQuery.read_method', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reshuffle', full_name='tensorflow_gnn.BigQuery.reshuffle', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BIGQUERY_TABLESPEC, ],
  enum_types=[
    _BIGQUERY_READMETHOD,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='source', full_name='tensorflow_gnn.BigQuery.source',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=792,
  serialized_end=1099,
)


_METADATA_KEYVALUE = _descriptor.Descriptor(
  name='KeyValue',
  full_name='tensorflow_gnn.Metadata.KeyValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow_gnn.Metadata.KeyValue.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow_gnn.Metadata.KeyValue.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1247,
  serialized_end=1285,
)

_METADATA = _descriptor.Descriptor(
  name='Metadata',
  full_name='tensorflow_gnn.Metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='extra', full_name='tensorflow_gnn.Metadata.extra', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filename', full_name='tensorflow_gnn.Metadata.filename', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cardinality', full_name='tensorflow_gnn.Metadata.cardinality', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bigquery', full_name='tensorflow_gnn.Metadata.bigquery', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_METADATA_KEYVALUE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1102,
  serialized_end=1285,
)


_CONTEXT_FEATURESENTRY = _descriptor.Descriptor(
  name='FeaturesEntry',
  full_name='tensorflow_gnn.Context.FeaturesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow_gnn.Context.FeaturesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow_gnn.Context.FeaturesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1400,
  serialized_end=1472,
)

_CONTEXT = _descriptor.Descriptor(
  name='Context',
  full_name='tensorflow_gnn.Context',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='features', full_name='tensorflow_gnn.Context.features', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='tensorflow_gnn.Context.metadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CONTEXT_FEATURESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1288,
  serialized_end=1472,
)


_NODESET_FEATURESENTRY = _descriptor.Descriptor(
  name='FeaturesEntry',
  full_name='tensorflow_gnn.NodeSet.FeaturesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow_gnn.NodeSet.FeaturesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow_gnn.NodeSet.FeaturesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1400,
  serialized_end=1472,
)

_NODESET = _descriptor.Descriptor(
  name='NodeSet',
  full_name='tensorflow_gnn.NodeSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='tensorflow_gnn.NodeSet.description', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='features', full_name='tensorflow_gnn.NodeSet.features', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='context', full_name='tensorflow_gnn.NodeSet.context', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='tensorflow_gnn.NodeSet.metadata', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_NODESET_FEATURESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1475,
  serialized_end=1697,
)


_EDGESET_FEATURESENTRY = _descriptor.Descriptor(
  name='FeaturesEntry',
  full_name='tensorflow_gnn.EdgeSet.FeaturesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow_gnn.EdgeSet.FeaturesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow_gnn.EdgeSet.FeaturesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1400,
  serialized_end=1472,
)

_EDGESET = _descriptor.Descriptor(
  name='EdgeSet',
  full_name='tensorflow_gnn.EdgeSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='tensorflow_gnn.EdgeSet.description', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='features', full_name='tensorflow_gnn.EdgeSet.features', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='tensorflow_gnn.EdgeSet.source', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target', full_name='tensorflow_gnn.EdgeSet.target', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='context', full_name='tensorflow_gnn.EdgeSet.context', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='tensorflow_gnn.EdgeSet.metadata', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EDGESET_FEATURESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1700,
  serialized_end=1954,
)


_ORIGININFO = _descriptor.Descriptor(
  name='OriginInfo',
  full_name='tensorflow_gnn.OriginInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='graph_type', full_name='tensorflow_gnn.OriginInfo.graph_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='root_set', full_name='tensorflow_gnn.OriginInfo.root_set', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1956,
  serialized_end=2033,
)

_GRAPHSCHEMA_NODESETSENTRY.fields_by_name['value'].message_type = _NODESET
_GRAPHSCHEMA_NODESETSENTRY.containing_type = _GRAPHSCHEMA
_GRAPHSCHEMA_EDGESETSENTRY.fields_by_name['value'].message_type = _EDGESET
_GRAPHSCHEMA_EDGESETSENTRY.containing_type = _GRAPHSCHEMA
_GRAPHSCHEMA.fields_by_name['context'].message_type = _CONTEXT
_GRAPHSCHEMA.fields_by_name['node_sets'].message_type = _GRAPHSCHEMA_NODESETSENTRY
_GRAPHSCHEMA.fields_by_name['edge_sets'].message_type = _GRAPHSCHEMA_EDGESETSENTRY
_GRAPHSCHEMA.fields_by_name['info'].message_type = _ORIGININFO
_FEATURE.fields_by_name['dtype'].enum_type = tensorflow_dot_core_dot_framework_dot_types__pb2._DATATYPE
_FEATURE.fields_by_name['shape'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2._TENSORSHAPEPROTO
_FEATURE.fields_by_name['sample_values'].message_type = tensorflow_dot_core_dot_example_dot_feature__pb2._FEATURE
_FEATURE.fields_by_name['example_values'].message_type = tensorflow_dot_core_dot_example_dot_feature__pb2._FEATURE
_BIGQUERY_TABLESPEC.containing_type = _BIGQUERY
_BIGQUERY.fields_by_name['table_spec'].message_type = _BIGQUERY_TABLESPEC
_BIGQUERY.fields_by_name['read_method'].enum_type = _BIGQUERY_READMETHOD
_BIGQUERY_READMETHOD.containing_type = _BIGQUERY
_BIGQUERY.oneofs_by_name['source'].fields.append(
  _BIGQUERY.fields_by_name['table_spec'])
_BIGQUERY.fields_by_name['table_spec'].containing_oneof = _BIGQUERY.oneofs_by_name['source']
_BIGQUERY.oneofs_by_name['source'].fields.append(
  _BIGQUERY.fields_by_name['sql'])
_BIGQUERY.fields_by_name['sql'].containing_oneof = _BIGQUERY.oneofs_by_name['source']
_METADATA_KEYVALUE.containing_type = _METADATA
_METADATA.fields_by_name['extra'].message_type = _METADATA_KEYVALUE
_METADATA.fields_by_name['bigquery'].message_type = _BIGQUERY
_CONTEXT_FEATURESENTRY.fields_by_name['value'].message_type = _FEATURE
_CONTEXT_FEATURESENTRY.containing_type = _CONTEXT
_CONTEXT.fields_by_name['features'].message_type = _CONTEXT_FEATURESENTRY
_CONTEXT.fields_by_name['metadata'].message_type = _METADATA
_NODESET_FEATURESENTRY.fields_by_name['value'].message_type = _FEATURE
_NODESET_FEATURESENTRY.containing_type = _NODESET
_NODESET.fields_by_name['features'].message_type = _NODESET_FEATURESENTRY
_NODESET.fields_by_name['metadata'].message_type = _METADATA
_EDGESET_FEATURESENTRY.fields_by_name['value'].message_type = _FEATURE
_EDGESET_FEATURESENTRY.containing_type = _EDGESET
_EDGESET.fields_by_name['features'].message_type = _EDGESET_FEATURESENTRY
_EDGESET.fields_by_name['metadata'].message_type = _METADATA
_ORIGININFO.fields_by_name['graph_type'].enum_type = _GRAPHTYPE
DESCRIPTOR.message_types_by_name['GraphSchema'] = _GRAPHSCHEMA
DESCRIPTOR.message_types_by_name['Feature'] = _FEATURE
DESCRIPTOR.message_types_by_name['BigQuery'] = _BIGQUERY
DESCRIPTOR.message_types_by_name['Metadata'] = _METADATA
DESCRIPTOR.message_types_by_name['Context'] = _CONTEXT
DESCRIPTOR.message_types_by_name['NodeSet'] = _NODESET
DESCRIPTOR.message_types_by_name['EdgeSet'] = _EDGESET
DESCRIPTOR.message_types_by_name['OriginInfo'] = _ORIGININFO
DESCRIPTOR.enum_types_by_name['SetType'] = _SETTYPE
DESCRIPTOR.enum_types_by_name['GraphType'] = _GRAPHTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GraphSchema = _reflection.GeneratedProtocolMessageType('GraphSchema', (_message.Message,), {

  'NodeSetsEntry' : _reflection.GeneratedProtocolMessageType('NodeSetsEntry', (_message.Message,), {
    'DESCRIPTOR' : _GRAPHSCHEMA_NODESETSENTRY,
    '__module__' : 'tensorflow_gnn.proto.graph_schema_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow_gnn.GraphSchema.NodeSetsEntry)
    })
  ,

  'EdgeSetsEntry' : _reflection.GeneratedProtocolMessageType('EdgeSetsEntry', (_message.Message,), {
    'DESCRIPTOR' : _GRAPHSCHEMA_EDGESETSENTRY,
    '__module__' : 'tensorflow_gnn.proto.graph_schema_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow_gnn.GraphSchema.EdgeSetsEntry)
    })
  ,
  'DESCRIPTOR' : _GRAPHSCHEMA,
  '__module__' : 'tensorflow_gnn.proto.graph_schema_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow_gnn.GraphSchema)
  })
_sym_db.RegisterMessage(GraphSchema)
_sym_db.RegisterMessage(GraphSchema.NodeSetsEntry)
_sym_db.RegisterMessage(GraphSchema.EdgeSetsEntry)

Feature = _reflection.GeneratedProtocolMessageType('Feature', (_message.Message,), {
  'DESCRIPTOR' : _FEATURE,
  '__module__' : 'tensorflow_gnn.proto.graph_schema_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow_gnn.Feature)
  })
_sym_db.RegisterMessage(Feature)

BigQuery = _reflection.GeneratedProtocolMessageType('BigQuery', (_message.Message,), {

  'TableSpec' : _reflection.GeneratedProtocolMessageType('TableSpec', (_message.Message,), {
    'DESCRIPTOR' : _BIGQUERY_TABLESPEC,
    '__module__' : 'tensorflow_gnn.proto.graph_schema_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow_gnn.BigQuery.TableSpec)
    })
  ,
  'DESCRIPTOR' : _BIGQUERY,
  '__module__' : 'tensorflow_gnn.proto.graph_schema_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow_gnn.BigQuery)
  })
_sym_db.RegisterMessage(BigQuery)
_sym_db.RegisterMessage(BigQuery.TableSpec)

Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), {

  'KeyValue' : _reflection.GeneratedProtocolMessageType('KeyValue', (_message.Message,), {
    'DESCRIPTOR' : _METADATA_KEYVALUE,
    '__module__' : 'tensorflow_gnn.proto.graph_schema_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow_gnn.Metadata.KeyValue)
    })
  ,
  'DESCRIPTOR' : _METADATA,
  '__module__' : 'tensorflow_gnn.proto.graph_schema_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow_gnn.Metadata)
  })
_sym_db.RegisterMessage(Metadata)
_sym_db.RegisterMessage(Metadata.KeyValue)

Context = _reflection.GeneratedProtocolMessageType('Context', (_message.Message,), {

  'FeaturesEntry' : _reflection.GeneratedProtocolMessageType('FeaturesEntry', (_message.Message,), {
    'DESCRIPTOR' : _CONTEXT_FEATURESENTRY,
    '__module__' : 'tensorflow_gnn.proto.graph_schema_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow_gnn.Context.FeaturesEntry)
    })
  ,
  'DESCRIPTOR' : _CONTEXT,
  '__module__' : 'tensorflow_gnn.proto.graph_schema_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow_gnn.Context)
  })
_sym_db.RegisterMessage(Context)
_sym_db.RegisterMessage(Context.FeaturesEntry)

NodeSet = _reflection.GeneratedProtocolMessageType('NodeSet', (_message.Message,), {

  'FeaturesEntry' : _reflection.GeneratedProtocolMessageType('FeaturesEntry', (_message.Message,), {
    'DESCRIPTOR' : _NODESET_FEATURESENTRY,
    '__module__' : 'tensorflow_gnn.proto.graph_schema_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow_gnn.NodeSet.FeaturesEntry)
    })
  ,
  'DESCRIPTOR' : _NODESET,
  '__module__' : 'tensorflow_gnn.proto.graph_schema_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow_gnn.NodeSet)
  })
_sym_db.RegisterMessage(NodeSet)
_sym_db.RegisterMessage(NodeSet.FeaturesEntry)

EdgeSet = _reflection.GeneratedProtocolMessageType('EdgeSet', (_message.Message,), {

  'FeaturesEntry' : _reflection.GeneratedProtocolMessageType('FeaturesEntry', (_message.Message,), {
    'DESCRIPTOR' : _EDGESET_FEATURESENTRY,
    '__module__' : 'tensorflow_gnn.proto.graph_schema_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow_gnn.EdgeSet.FeaturesEntry)
    })
  ,
  'DESCRIPTOR' : _EDGESET,
  '__module__' : 'tensorflow_gnn.proto.graph_schema_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow_gnn.EdgeSet)
  })
_sym_db.RegisterMessage(EdgeSet)
_sym_db.RegisterMessage(EdgeSet.FeaturesEntry)

OriginInfo = _reflection.GeneratedProtocolMessageType('OriginInfo', (_message.Message,), {
  'DESCRIPTOR' : _ORIGININFO,
  '__module__' : 'tensorflow_gnn.proto.graph_schema_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow_gnn.OriginInfo)
  })
_sym_db.RegisterMessage(OriginInfo)


_GRAPHSCHEMA_NODESETSENTRY._options = None
_GRAPHSCHEMA_EDGESETSENTRY._options = None
_FEATURE.fields_by_name['example_values']._options = None
_CONTEXT_FEATURESENTRY._options = None
_NODESET_FEATURESENTRY._options = None
_EDGESET_FEATURESENTRY._options = None
# @@protoc_insertion_point(module_scope)
