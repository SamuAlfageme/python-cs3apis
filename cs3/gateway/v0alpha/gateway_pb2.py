# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/gateway/v0alpha/gateway.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.appregistry.v0alpha import appregistry_pb2 as cs3_dot_appregistry_dot_v0alpha_dot_appregistry__pb2
from cs3.auth.v0alpha import auth_pb2 as cs3_dot_auth_dot_v0alpha_dot_auth__pb2
from cs3.ocmshareprovider.v0alpha import ocmshareprovider_pb2 as cs3_dot_ocmshareprovider_dot_v0alpha_dot_ocmshareprovider__pb2
from cs3.preferences.v0alpha import preferences_pb2 as cs3_dot_preferences_dot_v0alpha_dot_preferences__pb2
from cs3.publicshareprovider.v0alpha import publicshareprovider_pb2 as cs3_dot_publicshareprovider_dot_v0alpha_dot_publicshareprovider__pb2
from cs3.storageprovider.v0alpha import resources_pb2 as cs3_dot_storageprovider_dot_v0alpha_dot_resources__pb2
from cs3.storageprovider.v0alpha import storageprovider_pb2 as cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2
from cs3.types import types_pb2 as cs3_dot_types_dot_types__pb2
from cs3.usershareprovider.v0alpha import usershareprovider_pb2 as cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cs3/gateway/v0alpha/gateway.proto',
  package='cs3.gatewayv0alpha',
  syntax='proto3',
  serialized_options=_b('\n\026com.cs3.gatewayv0alphaB\014GatewayProtoP\001Z\020gatewayv0alphapb\242\002\006CBOXAB\252\002\022CS3.GatewayV0Alpha\312\002\022CS3\\GatewayV0Alpha'),
  serialized_pb=_b('\n!cs3/gateway/v0alpha/gateway.proto\x12\x12\x63s3.gatewayv0alpha\x1a)cs3/appregistry/v0alpha/appregistry.proto\x1a\x1b\x63s3/auth/v0alpha/auth.proto\x1a\x33\x63s3/ocmshareprovider/v0alpha/ocmshareprovider.proto\x1a)cs3/preferences/v0alpha/preferences.proto\x1a\x39\x63s3/publicshareprovider/v0alpha/publicshareprovider.proto\x1a+cs3/storageprovider/v0alpha/resources.proto\x1a\x31\x63s3/storageprovider/v0alpha/storageprovider.proto\x1a\x15\x63s3/types/types.proto\x1a\x35\x63s3/usershareprovider/v0alpha/usershareprovider.proto\"h\n\x0fGetQuotaRequest\x12!\n\x06opaque\x18\x01 \x01(\x0b\x32\x11.cs3.types.Opaque\x12\x32\n\x03ref\x18\x02 \x01(\x0b\x32%.cs3.storageproviderv0alpha.Reference\"\xb7\x01\n\x12ListRecycleRequest\x12!\n\x06opaque\x18\x01 \x01(\x0b\x32\x11.cs3.types.Opaque\x12\x32\n\x03ref\x18\x02 \x01(\x0b\x32%.cs3.storageproviderv0alpha.Reference\x12%\n\x07\x66rom_ts\x18\x03 \x01(\x0b\x32\x14.cs3.types.Timestamp\x12#\n\x05to_ts\x18\x04 \x01(\x0b\x32\x14.cs3.types.Timestamp\"\xbd\x01\n\x18ListRecycleStreamRequest\x12!\n\x06opaque\x18\x01 \x01(\x0b\x32\x11.cs3.types.Opaque\x12\x32\n\x03ref\x18\x02 \x01(\x0b\x32%.cs3.storageproviderv0alpha.Reference\x12%\n\x07\x66rom_ts\x18\x03 \x01(\x0b\x32\x14.cs3.types.Timestamp\x12#\n\x05to_ts\x18\x04 \x01(\x0b\x32\x14.cs3.types.Timestamp\"l\n\x13PurgeRecycleRequest\x12!\n\x06opaque\x18\x01 \x01(\x0b\x32\x11.cs3.types.Opaque\x12\x32\n\x03ref\x18\x02 \x01(\x0b\x32%.cs3.storageproviderv0alpha.Reference2\xdf*\n\x0eGatewayService\x12p\n\x13GenerateAccessToken\x12+.cs3.authv0alpha.GenerateAccessTokenRequest\x1a,.cs3.authv0alpha.GenerateAccessTokenResponse\x12I\n\x06WhoAmI\x12\x1e.cs3.authv0alpha.WhoAmIRequest\x1a\x1f.cs3.authv0alpha.WhoAmIResponse\x12z\n\x0f\x43reateContainer\x12\x32.cs3.storageproviderv0alpha.CreateContainerRequest\x1a\x33.cs3.storageproviderv0alpha.CreateContainerResponse\x12_\n\x06\x44\x65lete\x12).cs3.storageproviderv0alpha.DeleteRequest\x1a*.cs3.storageproviderv0alpha.DeleteResponse\x12\x62\n\x07GetPath\x12*.cs3.storageproviderv0alpha.GetPathRequest\x1a+.cs3.storageproviderv0alpha.GetPathResponse\x12]\n\x08GetQuota\x12#.cs3.gatewayv0alpha.GetQuotaRequest\x1a,.cs3.storageproviderv0alpha.GetQuotaResponse\x12\x89\x01\n\x14InitiateFileDownload\x12\x37.cs3.storageproviderv0alpha.InitiateFileDownloadRequest\x1a\x38.cs3.storageproviderv0alpha.InitiateFileDownloadResponse\x12\x83\x01\n\x12InitiateFileUpload\x12\x35.cs3.storageproviderv0alpha.InitiateFileUploadRequest\x1a\x36.cs3.storageproviderv0alpha.InitiateFileUploadResponse\x12\x88\x01\n\x13ListContainerStream\x12\x36.cs3.storageproviderv0alpha.ListContainerStreamRequest\x1a\x37.cs3.storageproviderv0alpha.ListContainerStreamResponse0\x01\x12t\n\rListContainer\x12\x30.cs3.storageproviderv0alpha.ListContainerRequest\x1a\x31.cs3.storageproviderv0alpha.ListContainerResponse\x12}\n\x10ListFileVersions\x12\x33.cs3.storageproviderv0alpha.ListFileVersionsRequest\x1a\x34.cs3.storageproviderv0alpha.ListFileVersionsResponse\x12z\n\x11ListRecycleStream\x12,.cs3.gatewayv0alpha.ListRecycleStreamRequest\x1a\x35.cs3.storageproviderv0alpha.ListRecycleStreamResponse0\x01\x12\x66\n\x0bListRecycle\x12&.cs3.gatewayv0alpha.ListRecycleRequest\x1a/.cs3.storageproviderv0alpha.ListRecycleResponse\x12Y\n\x04Move\x12\'.cs3.storageproviderv0alpha.MoveRequest\x1a(.cs3.storageproviderv0alpha.MoveResponse\x12i\n\x0cPurgeRecycle\x12\'.cs3.gatewayv0alpha.PurgeRecycleRequest\x1a\x30.cs3.storageproviderv0alpha.PurgeRecycleResponse\x12\x83\x01\n\x12RestoreFileVersion\x12\x35.cs3.storageproviderv0alpha.RestoreFileVersionRequest\x1a\x36.cs3.storageproviderv0alpha.RestoreFileVersionResponse\x12\x83\x01\n\x12RestoreRecycleItem\x12\x35.cs3.storageproviderv0alpha.RestoreRecycleItemRequest\x1a\x36.cs3.storageproviderv0alpha.RestoreRecycleItemResponse\x12Y\n\x04Stat\x12\'.cs3.storageproviderv0alpha.StatRequest\x1a(.cs3.storageproviderv0alpha.StatResponse\x12\x89\x01\n\x14SetArbitraryMetadata\x12\x37.cs3.storageproviderv0alpha.SetArbitraryMetadataRequest\x1a\x38.cs3.storageproviderv0alpha.SetArbitraryMetadataResponse\x12\x8f\x01\n\x16UnsetArbitraryMetadata\x12\x39.cs3.storageproviderv0alpha.UnsetArbitraryMetadataRequest\x1a:.cs3.storageproviderv0alpha.UnsetArbitraryMetadataResponse\x12r\n\x0b\x43reateShare\x12\x30.cs3.usershareproviderv0alpha.CreateShareRequest\x1a\x31.cs3.usershareproviderv0alpha.CreateShareResponse\x12r\n\x0bRemoveShare\x12\x30.cs3.usershareproviderv0alpha.RemoveShareRequest\x1a\x31.cs3.usershareproviderv0alpha.RemoveShareResponse\x12i\n\x08GetShare\x12-.cs3.usershareproviderv0alpha.GetShareRequest\x1a..cs3.usershareproviderv0alpha.GetShareResponse\x12o\n\nListShares\x12/.cs3.usershareproviderv0alpha.ListSharesRequest\x1a\x30.cs3.usershareproviderv0alpha.ListSharesResponse\x12r\n\x0bUpdateShare\x12\x30.cs3.usershareproviderv0alpha.UpdateShareRequest\x1a\x31.cs3.usershareproviderv0alpha.UpdateShareResponse\x12\x87\x01\n\x12ListReceivedShares\x12\x37.cs3.usershareproviderv0alpha.ListReceivedSharesRequest\x1a\x38.cs3.usershareproviderv0alpha.ListReceivedSharesResponse\x12\x8a\x01\n\x13UpdateReceivedShare\x12\x38.cs3.usershareproviderv0alpha.UpdateReceivedShareRequest\x1a\x39.cs3.usershareproviderv0alpha.UpdateReceivedShareResponse\x12\x81\x01\n\x10GetReceivedShare\x12\x35.cs3.usershareproviderv0alpha.GetReceivedShareRequest\x1a\x36.cs3.usershareproviderv0alpha.GetReceivedShareResponse\x12W\n\x06SetKey\x12%.cs3.preferencesv0alpha.SetKeyRequest\x1a&.cs3.preferencesv0alpha.SetKeyResponse\x12W\n\x06GetKey\x12%.cs3.preferencesv0alpha.GetKeyRequest\x1a&.cs3.preferencesv0alpha.GetKeyResponse\x12\x88\x01\n\x11\x43reatePublicShare\x12\x38.cs3.publicshareproviderv0alpha.CreatePublicShareRequest\x1a\x39.cs3.publicshareproviderv0alpha.CreatePublicShareResponse\x12\x88\x01\n\x11RemovePublicShare\x12\x38.cs3.publicshareproviderv0alpha.RemovePublicShareRequest\x1a\x39.cs3.publicshareproviderv0alpha.RemovePublicShareResponse\x12\x7f\n\x0eGetPublicShare\x12\x35.cs3.publicshareproviderv0alpha.GetPublicShareRequest\x1a\x36.cs3.publicshareproviderv0alpha.GetPublicShareResponse\x12\x94\x01\n\x15GetPublicShareByToken\x12<.cs3.publicshareproviderv0alpha.GetPublicShareByTokenRequest\x1a=.cs3.publicshareproviderv0alpha.GetPublicShareByTokenResponse\x12\x85\x01\n\x10ListPublicShares\x12\x37.cs3.publicshareproviderv0alpha.ListPublicSharesRequest\x1a\x38.cs3.publicshareproviderv0alpha.ListPublicSharesResponse\x12\x88\x01\n\x11UpdatePublicShare\x12\x38.cs3.publicshareproviderv0alpha.UpdatePublicShareRequest\x1a\x39.cs3.publicshareproviderv0alpha.UpdatePublicShareResponse\x12y\n\x0e\x43reateOCMShare\x12\x32.cs3.ocmshareproviderv0alpha.CreateOCMShareRequest\x1a\x33.cs3.ocmshareproviderv0alpha.CreateOCMShareResponse\x12y\n\x0eRemoveOCMShare\x12\x32.cs3.ocmshareproviderv0alpha.RemoveOCMShareRequest\x1a\x33.cs3.ocmshareproviderv0alpha.RemoveOCMShareResponse\x12p\n\x0bGetOCMShare\x12/.cs3.ocmshareproviderv0alpha.GetOCMShareRequest\x1a\x30.cs3.ocmshareproviderv0alpha.GetOCMShareResponse\x12v\n\rListOCMShares\x12\x31.cs3.ocmshareproviderv0alpha.ListOCMSharesRequest\x1a\x32.cs3.ocmshareproviderv0alpha.ListOCMSharesResponse\x12y\n\x0eUpdateOCMShare\x12\x32.cs3.ocmshareproviderv0alpha.UpdateOCMShareRequest\x1a\x33.cs3.ocmshareproviderv0alpha.UpdateOCMShareResponse\x12\x8e\x01\n\x15ListReceivedOCMShares\x12\x39.cs3.ocmshareproviderv0alpha.ListReceivedOCMSharesRequest\x1a:.cs3.ocmshareproviderv0alpha.ListReceivedOCMSharesResponse\x12\x91\x01\n\x16UpdateReceivedOCMShare\x12:.cs3.ocmshareproviderv0alpha.UpdateReceivedOCMShareRequest\x1a;.cs3.ocmshareproviderv0alpha.UpdateReceivedOCMShareResponse\x12r\n\x0fGetAppProviders\x12..cs3.appregistryv0alpha.GetAppProvidersRequest\x1a/.cs3.appregistryv0alpha.GetAppProvidersResponse\x12u\n\x10ListAppProviders\x12/.cs3.appregistryv0alpha.ListAppProvidersRequest\x1a\x30.cs3.appregistryv0alpha.ListAppProvidersResponseBm\n\x16\x63om.cs3.gatewayv0alphaB\x0cGatewayProtoP\x01Z\x10gatewayv0alphapb\xa2\x02\x06\x43\x42OXAB\xaa\x02\x12\x43S3.GatewayV0Alpha\xca\x02\x12\x43S3\\GatewayV0Alphab\x06proto3')
  ,
  dependencies=[cs3_dot_appregistry_dot_v0alpha_dot_appregistry__pb2.DESCRIPTOR,cs3_dot_auth_dot_v0alpha_dot_auth__pb2.DESCRIPTOR,cs3_dot_ocmshareprovider_dot_v0alpha_dot_ocmshareprovider__pb2.DESCRIPTOR,cs3_dot_preferences_dot_v0alpha_dot_preferences__pb2.DESCRIPTOR,cs3_dot_publicshareprovider_dot_v0alpha_dot_publicshareprovider__pb2.DESCRIPTOR,cs3_dot_storageprovider_dot_v0alpha_dot_resources__pb2.DESCRIPTOR,cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.DESCRIPTOR,cs3_dot_types_dot_types__pb2.DESCRIPTOR,cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.DESCRIPTOR,])




_GETQUOTAREQUEST = _descriptor.Descriptor(
  name='GetQuotaRequest',
  full_name='cs3.gatewayv0alpha.GetQuotaRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.gatewayv0alpha.GetQuotaRequest.opaque', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ref', full_name='cs3.gatewayv0alpha.GetQuotaRequest.ref', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=458,
  serialized_end=562,
)


_LISTRECYCLEREQUEST = _descriptor.Descriptor(
  name='ListRecycleRequest',
  full_name='cs3.gatewayv0alpha.ListRecycleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.gatewayv0alpha.ListRecycleRequest.opaque', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ref', full_name='cs3.gatewayv0alpha.ListRecycleRequest.ref', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='from_ts', full_name='cs3.gatewayv0alpha.ListRecycleRequest.from_ts', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to_ts', full_name='cs3.gatewayv0alpha.ListRecycleRequest.to_ts', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=565,
  serialized_end=748,
)


_LISTRECYCLESTREAMREQUEST = _descriptor.Descriptor(
  name='ListRecycleStreamRequest',
  full_name='cs3.gatewayv0alpha.ListRecycleStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.gatewayv0alpha.ListRecycleStreamRequest.opaque', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ref', full_name='cs3.gatewayv0alpha.ListRecycleStreamRequest.ref', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='from_ts', full_name='cs3.gatewayv0alpha.ListRecycleStreamRequest.from_ts', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to_ts', full_name='cs3.gatewayv0alpha.ListRecycleStreamRequest.to_ts', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=751,
  serialized_end=940,
)


_PURGERECYCLEREQUEST = _descriptor.Descriptor(
  name='PurgeRecycleRequest',
  full_name='cs3.gatewayv0alpha.PurgeRecycleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.gatewayv0alpha.PurgeRecycleRequest.opaque', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ref', full_name='cs3.gatewayv0alpha.PurgeRecycleRequest.ref', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=942,
  serialized_end=1050,
)

_GETQUOTAREQUEST.fields_by_name['opaque'].message_type = cs3_dot_types_dot_types__pb2._OPAQUE
_GETQUOTAREQUEST.fields_by_name['ref'].message_type = cs3_dot_storageprovider_dot_v0alpha_dot_resources__pb2._REFERENCE
_LISTRECYCLEREQUEST.fields_by_name['opaque'].message_type = cs3_dot_types_dot_types__pb2._OPAQUE
_LISTRECYCLEREQUEST.fields_by_name['ref'].message_type = cs3_dot_storageprovider_dot_v0alpha_dot_resources__pb2._REFERENCE
_LISTRECYCLEREQUEST.fields_by_name['from_ts'].message_type = cs3_dot_types_dot_types__pb2._TIMESTAMP
_LISTRECYCLEREQUEST.fields_by_name['to_ts'].message_type = cs3_dot_types_dot_types__pb2._TIMESTAMP
_LISTRECYCLESTREAMREQUEST.fields_by_name['opaque'].message_type = cs3_dot_types_dot_types__pb2._OPAQUE
_LISTRECYCLESTREAMREQUEST.fields_by_name['ref'].message_type = cs3_dot_storageprovider_dot_v0alpha_dot_resources__pb2._REFERENCE
_LISTRECYCLESTREAMREQUEST.fields_by_name['from_ts'].message_type = cs3_dot_types_dot_types__pb2._TIMESTAMP
_LISTRECYCLESTREAMREQUEST.fields_by_name['to_ts'].message_type = cs3_dot_types_dot_types__pb2._TIMESTAMP
_PURGERECYCLEREQUEST.fields_by_name['opaque'].message_type = cs3_dot_types_dot_types__pb2._OPAQUE
_PURGERECYCLEREQUEST.fields_by_name['ref'].message_type = cs3_dot_storageprovider_dot_v0alpha_dot_resources__pb2._REFERENCE
DESCRIPTOR.message_types_by_name['GetQuotaRequest'] = _GETQUOTAREQUEST
DESCRIPTOR.message_types_by_name['ListRecycleRequest'] = _LISTRECYCLEREQUEST
DESCRIPTOR.message_types_by_name['ListRecycleStreamRequest'] = _LISTRECYCLESTREAMREQUEST
DESCRIPTOR.message_types_by_name['PurgeRecycleRequest'] = _PURGERECYCLEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetQuotaRequest = _reflection.GeneratedProtocolMessageType('GetQuotaRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETQUOTAREQUEST,
  '__module__' : 'cs3.gateway.v0alpha.gateway_pb2'
  # @@protoc_insertion_point(class_scope:cs3.gatewayv0alpha.GetQuotaRequest)
  })
_sym_db.RegisterMessage(GetQuotaRequest)

ListRecycleRequest = _reflection.GeneratedProtocolMessageType('ListRecycleRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTRECYCLEREQUEST,
  '__module__' : 'cs3.gateway.v0alpha.gateway_pb2'
  # @@protoc_insertion_point(class_scope:cs3.gatewayv0alpha.ListRecycleRequest)
  })
_sym_db.RegisterMessage(ListRecycleRequest)

ListRecycleStreamRequest = _reflection.GeneratedProtocolMessageType('ListRecycleStreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTRECYCLESTREAMREQUEST,
  '__module__' : 'cs3.gateway.v0alpha.gateway_pb2'
  # @@protoc_insertion_point(class_scope:cs3.gatewayv0alpha.ListRecycleStreamRequest)
  })
_sym_db.RegisterMessage(ListRecycleStreamRequest)

PurgeRecycleRequest = _reflection.GeneratedProtocolMessageType('PurgeRecycleRequest', (_message.Message,), {
  'DESCRIPTOR' : _PURGERECYCLEREQUEST,
  '__module__' : 'cs3.gateway.v0alpha.gateway_pb2'
  # @@protoc_insertion_point(class_scope:cs3.gatewayv0alpha.PurgeRecycleRequest)
  })
_sym_db.RegisterMessage(PurgeRecycleRequest)


DESCRIPTOR._options = None

_GATEWAYSERVICE = _descriptor.ServiceDescriptor(
  name='GatewayService',
  full_name='cs3.gatewayv0alpha.GatewayService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1053,
  serialized_end=6524,
  methods=[
  _descriptor.MethodDescriptor(
    name='GenerateAccessToken',
    full_name='cs3.gatewayv0alpha.GatewayService.GenerateAccessToken',
    index=0,
    containing_service=None,
    input_type=cs3_dot_auth_dot_v0alpha_dot_auth__pb2._GENERATEACCESSTOKENREQUEST,
    output_type=cs3_dot_auth_dot_v0alpha_dot_auth__pb2._GENERATEACCESSTOKENRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='WhoAmI',
    full_name='cs3.gatewayv0alpha.GatewayService.WhoAmI',
    index=1,
    containing_service=None,
    input_type=cs3_dot_auth_dot_v0alpha_dot_auth__pb2._WHOAMIREQUEST,
    output_type=cs3_dot_auth_dot_v0alpha_dot_auth__pb2._WHOAMIRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateContainer',
    full_name='cs3.gatewayv0alpha.GatewayService.CreateContainer',
    index=2,
    containing_service=None,
    input_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._CREATECONTAINERREQUEST,
    output_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._CREATECONTAINERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='cs3.gatewayv0alpha.GatewayService.Delete',
    index=3,
    containing_service=None,
    input_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._DELETEREQUEST,
    output_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._DELETERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPath',
    full_name='cs3.gatewayv0alpha.GatewayService.GetPath',
    index=4,
    containing_service=None,
    input_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._GETPATHREQUEST,
    output_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._GETPATHRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetQuota',
    full_name='cs3.gatewayv0alpha.GatewayService.GetQuota',
    index=5,
    containing_service=None,
    input_type=_GETQUOTAREQUEST,
    output_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._GETQUOTARESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='InitiateFileDownload',
    full_name='cs3.gatewayv0alpha.GatewayService.InitiateFileDownload',
    index=6,
    containing_service=None,
    input_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._INITIATEFILEDOWNLOADREQUEST,
    output_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._INITIATEFILEDOWNLOADRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='InitiateFileUpload',
    full_name='cs3.gatewayv0alpha.GatewayService.InitiateFileUpload',
    index=7,
    containing_service=None,
    input_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._INITIATEFILEUPLOADREQUEST,
    output_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._INITIATEFILEUPLOADRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListContainerStream',
    full_name='cs3.gatewayv0alpha.GatewayService.ListContainerStream',
    index=8,
    containing_service=None,
    input_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._LISTCONTAINERSTREAMREQUEST,
    output_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._LISTCONTAINERSTREAMRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListContainer',
    full_name='cs3.gatewayv0alpha.GatewayService.ListContainer',
    index=9,
    containing_service=None,
    input_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._LISTCONTAINERREQUEST,
    output_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._LISTCONTAINERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListFileVersions',
    full_name='cs3.gatewayv0alpha.GatewayService.ListFileVersions',
    index=10,
    containing_service=None,
    input_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._LISTFILEVERSIONSREQUEST,
    output_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._LISTFILEVERSIONSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListRecycleStream',
    full_name='cs3.gatewayv0alpha.GatewayService.ListRecycleStream',
    index=11,
    containing_service=None,
    input_type=_LISTRECYCLESTREAMREQUEST,
    output_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._LISTRECYCLESTREAMRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListRecycle',
    full_name='cs3.gatewayv0alpha.GatewayService.ListRecycle',
    index=12,
    containing_service=None,
    input_type=_LISTRECYCLEREQUEST,
    output_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._LISTRECYCLERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Move',
    full_name='cs3.gatewayv0alpha.GatewayService.Move',
    index=13,
    containing_service=None,
    input_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._MOVEREQUEST,
    output_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._MOVERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PurgeRecycle',
    full_name='cs3.gatewayv0alpha.GatewayService.PurgeRecycle',
    index=14,
    containing_service=None,
    input_type=_PURGERECYCLEREQUEST,
    output_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._PURGERECYCLERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RestoreFileVersion',
    full_name='cs3.gatewayv0alpha.GatewayService.RestoreFileVersion',
    index=15,
    containing_service=None,
    input_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._RESTOREFILEVERSIONREQUEST,
    output_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._RESTOREFILEVERSIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RestoreRecycleItem',
    full_name='cs3.gatewayv0alpha.GatewayService.RestoreRecycleItem',
    index=16,
    containing_service=None,
    input_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._RESTORERECYCLEITEMREQUEST,
    output_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._RESTORERECYCLEITEMRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Stat',
    full_name='cs3.gatewayv0alpha.GatewayService.Stat',
    index=17,
    containing_service=None,
    input_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._STATREQUEST,
    output_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._STATRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetArbitraryMetadata',
    full_name='cs3.gatewayv0alpha.GatewayService.SetArbitraryMetadata',
    index=18,
    containing_service=None,
    input_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._SETARBITRARYMETADATAREQUEST,
    output_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._SETARBITRARYMETADATARESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UnsetArbitraryMetadata',
    full_name='cs3.gatewayv0alpha.GatewayService.UnsetArbitraryMetadata',
    index=19,
    containing_service=None,
    input_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._UNSETARBITRARYMETADATAREQUEST,
    output_type=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2._UNSETARBITRARYMETADATARESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateShare',
    full_name='cs3.gatewayv0alpha.GatewayService.CreateShare',
    index=20,
    containing_service=None,
    input_type=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2._CREATESHAREREQUEST,
    output_type=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2._CREATESHARERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveShare',
    full_name='cs3.gatewayv0alpha.GatewayService.RemoveShare',
    index=21,
    containing_service=None,
    input_type=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2._REMOVESHAREREQUEST,
    output_type=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2._REMOVESHARERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetShare',
    full_name='cs3.gatewayv0alpha.GatewayService.GetShare',
    index=22,
    containing_service=None,
    input_type=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2._GETSHAREREQUEST,
    output_type=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2._GETSHARERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListShares',
    full_name='cs3.gatewayv0alpha.GatewayService.ListShares',
    index=23,
    containing_service=None,
    input_type=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2._LISTSHARESREQUEST,
    output_type=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2._LISTSHARESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateShare',
    full_name='cs3.gatewayv0alpha.GatewayService.UpdateShare',
    index=24,
    containing_service=None,
    input_type=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2._UPDATESHAREREQUEST,
    output_type=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2._UPDATESHARERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListReceivedShares',
    full_name='cs3.gatewayv0alpha.GatewayService.ListReceivedShares',
    index=25,
    containing_service=None,
    input_type=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2._LISTRECEIVEDSHARESREQUEST,
    output_type=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2._LISTRECEIVEDSHARESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateReceivedShare',
    full_name='cs3.gatewayv0alpha.GatewayService.UpdateReceivedShare',
    index=26,
    containing_service=None,
    input_type=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2._UPDATERECEIVEDSHAREREQUEST,
    output_type=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2._UPDATERECEIVEDSHARERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetReceivedShare',
    full_name='cs3.gatewayv0alpha.GatewayService.GetReceivedShare',
    index=27,
    containing_service=None,
    input_type=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2._GETRECEIVEDSHAREREQUEST,
    output_type=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2._GETRECEIVEDSHARERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetKey',
    full_name='cs3.gatewayv0alpha.GatewayService.SetKey',
    index=28,
    containing_service=None,
    input_type=cs3_dot_preferences_dot_v0alpha_dot_preferences__pb2._SETKEYREQUEST,
    output_type=cs3_dot_preferences_dot_v0alpha_dot_preferences__pb2._SETKEYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetKey',
    full_name='cs3.gatewayv0alpha.GatewayService.GetKey',
    index=29,
    containing_service=None,
    input_type=cs3_dot_preferences_dot_v0alpha_dot_preferences__pb2._GETKEYREQUEST,
    output_type=cs3_dot_preferences_dot_v0alpha_dot_preferences__pb2._GETKEYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreatePublicShare',
    full_name='cs3.gatewayv0alpha.GatewayService.CreatePublicShare',
    index=30,
    containing_service=None,
    input_type=cs3_dot_publicshareprovider_dot_v0alpha_dot_publicshareprovider__pb2._CREATEPUBLICSHAREREQUEST,
    output_type=cs3_dot_publicshareprovider_dot_v0alpha_dot_publicshareprovider__pb2._CREATEPUBLICSHARERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RemovePublicShare',
    full_name='cs3.gatewayv0alpha.GatewayService.RemovePublicShare',
    index=31,
    containing_service=None,
    input_type=cs3_dot_publicshareprovider_dot_v0alpha_dot_publicshareprovider__pb2._REMOVEPUBLICSHAREREQUEST,
    output_type=cs3_dot_publicshareprovider_dot_v0alpha_dot_publicshareprovider__pb2._REMOVEPUBLICSHARERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPublicShare',
    full_name='cs3.gatewayv0alpha.GatewayService.GetPublicShare',
    index=32,
    containing_service=None,
    input_type=cs3_dot_publicshareprovider_dot_v0alpha_dot_publicshareprovider__pb2._GETPUBLICSHAREREQUEST,
    output_type=cs3_dot_publicshareprovider_dot_v0alpha_dot_publicshareprovider__pb2._GETPUBLICSHARERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPublicShareByToken',
    full_name='cs3.gatewayv0alpha.GatewayService.GetPublicShareByToken',
    index=33,
    containing_service=None,
    input_type=cs3_dot_publicshareprovider_dot_v0alpha_dot_publicshareprovider__pb2._GETPUBLICSHAREBYTOKENREQUEST,
    output_type=cs3_dot_publicshareprovider_dot_v0alpha_dot_publicshareprovider__pb2._GETPUBLICSHAREBYTOKENRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListPublicShares',
    full_name='cs3.gatewayv0alpha.GatewayService.ListPublicShares',
    index=34,
    containing_service=None,
    input_type=cs3_dot_publicshareprovider_dot_v0alpha_dot_publicshareprovider__pb2._LISTPUBLICSHARESREQUEST,
    output_type=cs3_dot_publicshareprovider_dot_v0alpha_dot_publicshareprovider__pb2._LISTPUBLICSHARESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdatePublicShare',
    full_name='cs3.gatewayv0alpha.GatewayService.UpdatePublicShare',
    index=35,
    containing_service=None,
    input_type=cs3_dot_publicshareprovider_dot_v0alpha_dot_publicshareprovider__pb2._UPDATEPUBLICSHAREREQUEST,
    output_type=cs3_dot_publicshareprovider_dot_v0alpha_dot_publicshareprovider__pb2._UPDATEPUBLICSHARERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateOCMShare',
    full_name='cs3.gatewayv0alpha.GatewayService.CreateOCMShare',
    index=36,
    containing_service=None,
    input_type=cs3_dot_ocmshareprovider_dot_v0alpha_dot_ocmshareprovider__pb2._CREATEOCMSHAREREQUEST,
    output_type=cs3_dot_ocmshareprovider_dot_v0alpha_dot_ocmshareprovider__pb2._CREATEOCMSHARERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveOCMShare',
    full_name='cs3.gatewayv0alpha.GatewayService.RemoveOCMShare',
    index=37,
    containing_service=None,
    input_type=cs3_dot_ocmshareprovider_dot_v0alpha_dot_ocmshareprovider__pb2._REMOVEOCMSHAREREQUEST,
    output_type=cs3_dot_ocmshareprovider_dot_v0alpha_dot_ocmshareprovider__pb2._REMOVEOCMSHARERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetOCMShare',
    full_name='cs3.gatewayv0alpha.GatewayService.GetOCMShare',
    index=38,
    containing_service=None,
    input_type=cs3_dot_ocmshareprovider_dot_v0alpha_dot_ocmshareprovider__pb2._GETOCMSHAREREQUEST,
    output_type=cs3_dot_ocmshareprovider_dot_v0alpha_dot_ocmshareprovider__pb2._GETOCMSHARERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListOCMShares',
    full_name='cs3.gatewayv0alpha.GatewayService.ListOCMShares',
    index=39,
    containing_service=None,
    input_type=cs3_dot_ocmshareprovider_dot_v0alpha_dot_ocmshareprovider__pb2._LISTOCMSHARESREQUEST,
    output_type=cs3_dot_ocmshareprovider_dot_v0alpha_dot_ocmshareprovider__pb2._LISTOCMSHARESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateOCMShare',
    full_name='cs3.gatewayv0alpha.GatewayService.UpdateOCMShare',
    index=40,
    containing_service=None,
    input_type=cs3_dot_ocmshareprovider_dot_v0alpha_dot_ocmshareprovider__pb2._UPDATEOCMSHAREREQUEST,
    output_type=cs3_dot_ocmshareprovider_dot_v0alpha_dot_ocmshareprovider__pb2._UPDATEOCMSHARERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListReceivedOCMShares',
    full_name='cs3.gatewayv0alpha.GatewayService.ListReceivedOCMShares',
    index=41,
    containing_service=None,
    input_type=cs3_dot_ocmshareprovider_dot_v0alpha_dot_ocmshareprovider__pb2._LISTRECEIVEDOCMSHARESREQUEST,
    output_type=cs3_dot_ocmshareprovider_dot_v0alpha_dot_ocmshareprovider__pb2._LISTRECEIVEDOCMSHARESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateReceivedOCMShare',
    full_name='cs3.gatewayv0alpha.GatewayService.UpdateReceivedOCMShare',
    index=42,
    containing_service=None,
    input_type=cs3_dot_ocmshareprovider_dot_v0alpha_dot_ocmshareprovider__pb2._UPDATERECEIVEDOCMSHAREREQUEST,
    output_type=cs3_dot_ocmshareprovider_dot_v0alpha_dot_ocmshareprovider__pb2._UPDATERECEIVEDOCMSHARERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetAppProviders',
    full_name='cs3.gatewayv0alpha.GatewayService.GetAppProviders',
    index=43,
    containing_service=None,
    input_type=cs3_dot_appregistry_dot_v0alpha_dot_appregistry__pb2._GETAPPPROVIDERSREQUEST,
    output_type=cs3_dot_appregistry_dot_v0alpha_dot_appregistry__pb2._GETAPPPROVIDERSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListAppProviders',
    full_name='cs3.gatewayv0alpha.GatewayService.ListAppProviders',
    index=44,
    containing_service=None,
    input_type=cs3_dot_appregistry_dot_v0alpha_dot_appregistry__pb2._LISTAPPPROVIDERSREQUEST,
    output_type=cs3_dot_appregistry_dot_v0alpha_dot_appregistry__pb2._LISTAPPPROVIDERSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GATEWAYSERVICE)

DESCRIPTOR.services_by_name['GatewayService'] = _GATEWAYSERVICE

# @@protoc_insertion_point(module_scope)
