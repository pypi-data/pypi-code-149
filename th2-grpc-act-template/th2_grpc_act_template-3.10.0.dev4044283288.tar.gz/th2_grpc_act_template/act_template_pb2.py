# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: th2_grpc_act_template/act_template.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from th2_grpc_common import common_pb2 as th2__grpc__common_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(th2_grpc_act_template/act_template.proto\x1a\x1cth2_grpc_common/common.proto\"Y\n\x13SendMessageResponse\x12\x1e\n\x06status\x18\x01 \x01(\x0b\x32\x0e.RequestStatus\x12\"\n\rcheckpoint_id\x18\x02 \x01(\x0b\x32\x0b.Checkpoint\"\x92\x01\n\x13PlaceMessageRequest\x12\x19\n\x07message\x18\x01 \x01(\x0b\x32\x08.Message\x12(\n\rconnection_id\x18\x02 \x01(\x0b\x32\r.ConnectionIDB\x02\x18\x01\x12!\n\x0fparent_event_id\x18\x04 \x01(\x0b\x32\x08.EventID\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\"~\n\x14PlaceMessageResponse\x12\"\n\x10response_message\x18\x01 \x01(\x0b\x32\x08.Message\x12\x1e\n\x06status\x18\x02 \x01(\x0b\x32\x0e.RequestStatus\x12\"\n\rcheckpoint_id\x18\x03 \x01(\x0b\x32\x0b.Checkpoint2\xd0\x05\n\x03\x41\x63t\x12>\n\rplaceOrderFIX\x12\x14.PlaceMessageRequest\x1a\x15.PlaceMessageResponse\"\x00\x12H\n\x17placeOrderCancelRequest\x12\x14.PlaceMessageRequest\x1a\x15.PlaceMessageResponse\"\x00\x12O\n\x1eplaceOrderCancelReplaceRequest\x12\x14.PlaceMessageRequest\x1a\x15.PlaceMessageResponse\"\x00\x12;\n\x0bsendMessage\x12\x14.PlaceMessageRequest\x1a\x14.SendMessageResponse\"\x00\x12\x45\n\x14placeQuoteRequestFIX\x12\x14.PlaceMessageRequest\x1a\x15.PlaceMessageResponse\"\x00\x12>\n\rplaceQuoteFIX\x12\x14.PlaceMessageRequest\x1a\x15.PlaceMessageResponse\"\x00\x12O\n\x1eplaceOrderMassCancelRequestFIX\x12\x14.PlaceMessageRequest\x1a\x15.PlaceMessageResponse\"\x00\x12\x44\n\x13placeQuoteCancelFIX\x12\x14.PlaceMessageRequest\x1a\x15.PlaceMessageResponse\"\x00\x12\x46\n\x15placeQuoteResponseFIX\x12\x14.PlaceMessageRequest\x1a\x15.PlaceMessageResponse\"\x00\x12K\n\x1aplaceSecurityStatusRequest\x12\x14.PlaceMessageRequest\x1a\x15.PlaceMessageResponse\"\x00\x42\x1d\n\x19\x63om.exactpro.th2.act.grpcP\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'th2_grpc_act_template.act_template_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.exactpro.th2.act.grpcP\001'
  _PLACEMESSAGEREQUEST.fields_by_name['connection_id']._options = None
  _PLACEMESSAGEREQUEST.fields_by_name['connection_id']._serialized_options = b'\030\001'
  _SENDMESSAGERESPONSE._serialized_start=74
  _SENDMESSAGERESPONSE._serialized_end=163
  _PLACEMESSAGEREQUEST._serialized_start=166
  _PLACEMESSAGEREQUEST._serialized_end=312
  _PLACEMESSAGERESPONSE._serialized_start=314
  _PLACEMESSAGERESPONSE._serialized_end=440
  _ACT._serialized_start=443
  _ACT._serialized_end=1163
# @@protoc_insertion_point(module_scope)
