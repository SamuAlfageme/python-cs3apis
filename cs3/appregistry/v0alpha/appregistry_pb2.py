# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/appregistry/v0alpha/appregistry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.appregistry.v0alpha import resources_pb2 as cs3_dot_appregistry_dot_v0alpha_dot_resources__pb2
from cs3.rpc import status_pb2 as cs3_dot_rpc_dot_status__pb2
from cs3.storageprovider.v0alpha import resources_pb2 as cs3_dot_storageprovider_dot_v0alpha_dot_resources__pb2
from cs3.types import types_pb2 as cs3_dot_types_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cs3/appregistry/v0alpha/appregistry.proto',
  package='cs3.appregistryv0alpha',
  syntax='proto3',
  serialized_options=_b('\n\032com.cs3.appregistryv0alphaB\020AppregistryProtoP\001Z\024appregistryv0alphapb\242\002\017CBOXAPPREGISTRY\252\002\026CS3.AppRegistryV0Alpha\312\002\026CS3\\AppRegistryV0Alpha'),
  serialized_pb=_b('\n)cs3/appregistry/v0alpha/appregistry.proto\x12\x16\x63s3.appregistryv0alpha\x1a\'cs3/appregistry/v0alpha/resources.proto\x1a\x14\x63s3/rpc/status.proto\x1a+cs3/storageprovider/v0alpha/resources.proto\x1a\x15\x63s3/types/types.proto\"|\n\x16GetAppProvidersRequest\x12!\n\x06opaque\x18\x01 \x01(\x0b\x32\x11.cs3.types.Opaque\x12?\n\rresource_info\x18\x02 \x01(\x0b\x32(.cs3.storageproviderv0alpha.ResourceInfo\"\x96\x01\n\x17GetAppProvidersResponse\x12\x1f\n\x06status\x18\x01 \x01(\x0b\x32\x0f.cs3.rpc.Status\x12!\n\x06opaque\x18\x02 \x01(\x0b\x32\x11.cs3.types.Opaque\x12\x37\n\tproviders\x18\x03 \x03(\x0b\x32$.cs3.appregistryv0alpha.ProviderInfo\"<\n\x17ListAppProvidersRequest\x12!\n\x06opaque\x18\x01 \x01(\x0b\x32\x11.cs3.types.Opaque\"\x97\x01\n\x18ListAppProvidersResponse\x12\x1f\n\x06status\x18\x01 \x01(\x0b\x32\x0f.cs3.rpc.Status\x12!\n\x06opaque\x18\x02 \x01(\x0b\x32\x11.cs3.types.Opaque\x12\x37\n\tproviders\x18\x03 \x03(\x0b\x32$.cs3.appregistryv0alpha.ProviderInfo2\xff\x01\n\x12\x41ppRegistryService\x12r\n\x0fGetAppProviders\x12..cs3.appregistryv0alpha.GetAppProvidersRequest\x1a/.cs3.appregistryv0alpha.GetAppProvidersResponse\x12u\n\x10ListAppProviders\x12/.cs3.appregistryv0alpha.ListAppProvidersRequest\x1a\x30.cs3.appregistryv0alpha.ListAppProvidersResponseB\x8a\x01\n\x1a\x63om.cs3.appregistryv0alphaB\x10\x41ppregistryProtoP\x01Z\x14\x61ppregistryv0alphapb\xa2\x02\x0f\x43\x42OXAPPREGISTRY\xaa\x02\x16\x43S3.AppRegistryV0Alpha\xca\x02\x16\x43S3\\AppRegistryV0Alphab\x06proto3')
  ,
  dependencies=[cs3_dot_appregistry_dot_v0alpha_dot_resources__pb2.DESCRIPTOR,cs3_dot_rpc_dot_status__pb2.DESCRIPTOR,cs3_dot_storageprovider_dot_v0alpha_dot_resources__pb2.DESCRIPTOR,cs3_dot_types_dot_types__pb2.DESCRIPTOR,])




_GETAPPPROVIDERSREQUEST = _descriptor.Descriptor(
  name='GetAppProvidersRequest',
  full_name='cs3.appregistryv0alpha.GetAppProvidersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.appregistryv0alpha.GetAppProvidersRequest.opaque', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource_info', full_name='cs3.appregistryv0alpha.GetAppProvidersRequest.resource_info', index=1,
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
  serialized_start=200,
  serialized_end=324,
)


_GETAPPPROVIDERSRESPONSE = _descriptor.Descriptor(
  name='GetAppProvidersResponse',
  full_name='cs3.appregistryv0alpha.GetAppProvidersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cs3.appregistryv0alpha.GetAppProvidersResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.appregistryv0alpha.GetAppProvidersResponse.opaque', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='providers', full_name='cs3.appregistryv0alpha.GetAppProvidersResponse.providers', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=327,
  serialized_end=477,
)


_LISTAPPPROVIDERSREQUEST = _descriptor.Descriptor(
  name='ListAppProvidersRequest',
  full_name='cs3.appregistryv0alpha.ListAppProvidersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.appregistryv0alpha.ListAppProvidersRequest.opaque', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=479,
  serialized_end=539,
)


_LISTAPPPROVIDERSRESPONSE = _descriptor.Descriptor(
  name='ListAppProvidersResponse',
  full_name='cs3.appregistryv0alpha.ListAppProvidersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cs3.appregistryv0alpha.ListAppProvidersResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.appregistryv0alpha.ListAppProvidersResponse.opaque', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='providers', full_name='cs3.appregistryv0alpha.ListAppProvidersResponse.providers', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=542,
  serialized_end=693,
)

_GETAPPPROVIDERSREQUEST.fields_by_name['opaque'].message_type = cs3_dot_types_dot_types__pb2._OPAQUE
_GETAPPPROVIDERSREQUEST.fields_by_name['resource_info'].message_type = cs3_dot_storageprovider_dot_v0alpha_dot_resources__pb2._RESOURCEINFO
_GETAPPPROVIDERSRESPONSE.fields_by_name['status'].message_type = cs3_dot_rpc_dot_status__pb2._STATUS
_GETAPPPROVIDERSRESPONSE.fields_by_name['opaque'].message_type = cs3_dot_types_dot_types__pb2._OPAQUE
_GETAPPPROVIDERSRESPONSE.fields_by_name['providers'].message_type = cs3_dot_appregistry_dot_v0alpha_dot_resources__pb2._PROVIDERINFO
_LISTAPPPROVIDERSREQUEST.fields_by_name['opaque'].message_type = cs3_dot_types_dot_types__pb2._OPAQUE
_LISTAPPPROVIDERSRESPONSE.fields_by_name['status'].message_type = cs3_dot_rpc_dot_status__pb2._STATUS
_LISTAPPPROVIDERSRESPONSE.fields_by_name['opaque'].message_type = cs3_dot_types_dot_types__pb2._OPAQUE
_LISTAPPPROVIDERSRESPONSE.fields_by_name['providers'].message_type = cs3_dot_appregistry_dot_v0alpha_dot_resources__pb2._PROVIDERINFO
DESCRIPTOR.message_types_by_name['GetAppProvidersRequest'] = _GETAPPPROVIDERSREQUEST
DESCRIPTOR.message_types_by_name['GetAppProvidersResponse'] = _GETAPPPROVIDERSRESPONSE
DESCRIPTOR.message_types_by_name['ListAppProvidersRequest'] = _LISTAPPPROVIDERSREQUEST
DESCRIPTOR.message_types_by_name['ListAppProvidersResponse'] = _LISTAPPPROVIDERSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAppProvidersRequest = _reflection.GeneratedProtocolMessageType('GetAppProvidersRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETAPPPROVIDERSREQUEST,
  '__module__' : 'cs3.appregistry.v0alpha.appregistry_pb2'
  # @@protoc_insertion_point(class_scope:cs3.appregistryv0alpha.GetAppProvidersRequest)
  })
_sym_db.RegisterMessage(GetAppProvidersRequest)

GetAppProvidersResponse = _reflection.GeneratedProtocolMessageType('GetAppProvidersResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETAPPPROVIDERSRESPONSE,
  '__module__' : 'cs3.appregistry.v0alpha.appregistry_pb2'
  # @@protoc_insertion_point(class_scope:cs3.appregistryv0alpha.GetAppProvidersResponse)
  })
_sym_db.RegisterMessage(GetAppProvidersResponse)

ListAppProvidersRequest = _reflection.GeneratedProtocolMessageType('ListAppProvidersRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTAPPPROVIDERSREQUEST,
  '__module__' : 'cs3.appregistry.v0alpha.appregistry_pb2'
  # @@protoc_insertion_point(class_scope:cs3.appregistryv0alpha.ListAppProvidersRequest)
  })
_sym_db.RegisterMessage(ListAppProvidersRequest)

ListAppProvidersResponse = _reflection.GeneratedProtocolMessageType('ListAppProvidersResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTAPPPROVIDERSRESPONSE,
  '__module__' : 'cs3.appregistry.v0alpha.appregistry_pb2'
  # @@protoc_insertion_point(class_scope:cs3.appregistryv0alpha.ListAppProvidersResponse)
  })
_sym_db.RegisterMessage(ListAppProvidersResponse)


DESCRIPTOR._options = None

_APPREGISTRYSERVICE = _descriptor.ServiceDescriptor(
  name='AppRegistryService',
  full_name='cs3.appregistryv0alpha.AppRegistryService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=696,
  serialized_end=951,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAppProviders',
    full_name='cs3.appregistryv0alpha.AppRegistryService.GetAppProviders',
    index=0,
    containing_service=None,
    input_type=_GETAPPPROVIDERSREQUEST,
    output_type=_GETAPPPROVIDERSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListAppProviders',
    full_name='cs3.appregistryv0alpha.AppRegistryService.ListAppProviders',
    index=1,
    containing_service=None,
    input_type=_LISTAPPPROVIDERSREQUEST,
    output_type=_LISTAPPPROVIDERSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_APPREGISTRYSERVICE)

DESCRIPTOR.services_by_name['AppRegistryService'] = _APPREGISTRYSERVICE

# @@protoc_insertion_point(module_scope)
