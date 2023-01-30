# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/admin/description_entity.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flyteidl.core import identifier_pb2 as flyteidl_dot_core_dot_identifier__pb2
from flyteidl.admin import common_pb2 as flyteidl_dot_admin_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'flyteidl/admin/description_entity.proto\x12\x0e\x66lyteidl.admin\x1a\x1e\x66lyteidl/core/identifier.proto\x1a\x1b\x66lyteidl/admin/common.proto\"\x84\x02\n\x11\x44\x65scriptionEntity\x12)\n\x02id\x18\x01 \x01(\x0b\x32\x19.flyteidl.core.IdentifierR\x02id\x12+\n\x11short_description\x18\x02 \x01(\tR\x10shortDescription\x12\x46\n\x10long_description\x18\x03 \x01(\x0b\x32\x1b.flyteidl.admin.DescriptionR\x0flongDescription\x12;\n\x0bsource_code\x18\x04 \x01(\x0b\x32\x1a.flyteidl.admin.SourceCodeR\nsourceCode\x12\x12\n\x04tags\x18\x05 \x03(\tR\x04tags\"\x9c\x01\n\x0b\x44\x65scription\x12\x16\n\x05value\x18\x01 \x01(\tH\x00R\x05value\x12\x12\n\x03uri\x18\x02 \x01(\tH\x00R\x03uri\x12\x39\n\x06\x66ormat\x18\x03 \x01(\x0e\x32!.flyteidl.admin.DescriptionFormatR\x06\x66ormat\x12\x1b\n\ticon_link\x18\x04 \x01(\tR\x08iconLinkB\t\n\x07\x63ontent\" \n\nSourceCode\x12\x12\n\x04link\x18\x01 \x01(\tR\x04link\"\x82\x01\n\x15\x44\x65scriptionEntityList\x12S\n\x13\x64\x65scriptionEntities\x18\x01 \x03(\x0b\x32!.flyteidl.admin.DescriptionEntityR\x13\x64\x65scriptionEntities\x12\x14\n\x05token\x18\x02 \x01(\tR\x05token\"\x8c\x02\n\x1c\x44\x65scriptionEntityListRequest\x12@\n\rresource_type\x18\x01 \x01(\x0e\x32\x1b.flyteidl.core.ResourceTypeR\x0cresourceType\x12\x35\n\x02id\x18\x02 \x01(\x0b\x32%.flyteidl.admin.NamedEntityIdentifierR\x02id\x12\x14\n\x05limit\x18\x03 \x01(\rR\x05limit\x12\x14\n\x05token\x18\x04 \x01(\tR\x05token\x12\x18\n\x07\x66ilters\x18\x05 \x01(\tR\x07\x66ilters\x12-\n\x07sort_by\x18\x06 \x01(\x0b\x32\x14.flyteidl.admin.SortR\x06sortBy*\x8d\x01\n\x11\x44\x65scriptionFormat\x12\x1e\n\x1a\x44\x45SCRIPTION_FORMAT_UNKNOWN\x10\x00\x12\x1f\n\x1b\x44\x45SCRIPTION_FORMAT_MARKDOWN\x10\x01\x12\x1b\n\x17\x44\x45SCRIPTION_FORMAT_HTML\x10\x02\x12\x1a\n\x16\x44\x45SCRIPTION_FORMAT_RST\x10\x03\x42\xbc\x01\n\x12\x63om.flyteidl.adminB\x16\x44\x65scriptionEntityProtoP\x01Z5github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/admin\xa2\x02\x03\x46\x41X\xaa\x02\x0e\x46lyteidl.Admin\xca\x02\x0e\x46lyteidl\\Admin\xe2\x02\x1a\x46lyteidl\\Admin\\GPBMetadata\xea\x02\x0f\x46lyteidl::Adminb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flyteidl.admin.description_entity_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022com.flyteidl.adminB\026DescriptionEntityProtoP\001Z5github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/admin\242\002\003FAX\252\002\016Flyteidl.Admin\312\002\016Flyteidl\\Admin\342\002\032Flyteidl\\Admin\\GPBMetadata\352\002\017Flyteidl::Admin'
  _DESCRIPTIONFORMAT._serialized_start=981
  _DESCRIPTIONFORMAT._serialized_end=1122
  _DESCRIPTIONENTITY._serialized_start=121
  _DESCRIPTIONENTITY._serialized_end=381
  _DESCRIPTION._serialized_start=384
  _DESCRIPTION._serialized_end=540
  _SOURCECODE._serialized_start=542
  _SOURCECODE._serialized_end=574
  _DESCRIPTIONENTITYLIST._serialized_start=577
  _DESCRIPTIONENTITYLIST._serialized_end=707
  _DESCRIPTIONENTITYLISTREQUEST._serialized_start=710
  _DESCRIPTIONENTITYLISTREQUEST._serialized_end=978
# @@protoc_insertion_point(module_scope)
