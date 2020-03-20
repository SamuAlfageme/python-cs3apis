# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/sharing/ocm/v1beta1/resources.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.identity.user.v1beta1 import resources_pb2 as cs3_dot_identity_dot_user_dot_v1beta1_dot_resources__pb2
from cs3.storage.provider.v1beta1 import resources_pb2 as cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2
from cs3.types.v1beta1 import types_pb2 as cs3_dot_types_dot_v1beta1_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cs3/sharing/ocm/v1beta1/resources.proto',
  package='cs3.sharing.ocm.v1beta1',
  syntax='proto3',
  serialized_options=_b('\n\033com.cs3.sharing.ocm.v1beta1B\016ResourcesProtoP\001Z\nocmv1beta1\242\002\003CSO\252\002\027Cs3.Sharing.Ocm.V1Beta1\312\002\027Cs3\\Sharing\\Ocm\\V1Beta1'),
  serialized_pb=_b('\n\'cs3/sharing/ocm/v1beta1/resources.proto\x12\x17\x63s3.sharing.ocm.v1beta1\x1a)cs3/identity/user/v1beta1/resources.proto\x1a,cs3/storage/provider/v1beta1/resources.proto\x1a\x1d\x63s3/types/v1beta1/types.proto\"\xac\x03\n\x05Share\x12,\n\x02id\x18\x01 \x01(\x0b\x32 .cs3.sharing.ocm.v1beta1.ShareId\x12=\n\x0bresource_id\x18\x02 \x01(\x0b\x32(.cs3.storage.provider.v1beta1.ResourceId\x12>\n\x0bpermissions\x18\x03 \x01(\x0b\x32).cs3.sharing.ocm.v1beta1.SharePermissions\x12\x36\n\x07grantee\x18\x04 \x01(\x0b\x32%.cs3.storage.provider.v1beta1.Grantee\x12\x30\n\x05owner\x18\x05 \x01(\x0b\x32!.cs3.identity.user.v1beta1.UserId\x12\x32\n\x07\x63reator\x18\x06 \x01(\x0b\x32!.cs3.identity.user.v1beta1.UserId\x12+\n\x05\x63time\x18\x07 \x01(\x0b\x32\x1c.cs3.types.v1beta1.Timestamp\x12+\n\x05mtime\x18\x08 \x01(\x0b\x32\x1c.cs3.types.v1beta1.Timestamp\"k\n\x10SharePermissions\x12\x46\n\x0bpermissions\x18\x01 \x01(\x0b\x32\x31.cs3.storage.provider.v1beta1.ResourcePermissions\x12\x0f\n\x07reshare\x18\x02 \x01(\x08\"r\n\rReceivedShare\x12-\n\x05share\x18\x01 \x01(\x0b\x32\x1e.cs3.sharing.ocm.v1beta1.Share\x12\x32\n\x05state\x18\x02 \x01(\x0e\x32#.cs3.sharing.ocm.v1beta1.ShareState\"\xb3\x01\n\x08ShareKey\x12\x30\n\x05owner\x18\x02 \x01(\x0b\x32!.cs3.identity.user.v1beta1.UserId\x12=\n\x0bresource_id\x18\x03 \x01(\x0b\x32(.cs3.storage.provider.v1beta1.ResourceId\x12\x36\n\x07grantee\x18\x04 \x01(\x0b\x32%.cs3.storage.provider.v1beta1.Grantee\"\x1c\n\x07ShareId\x12\x11\n\topaque_id\x18\x02 \x01(\t\"z\n\x0eShareReference\x12.\n\x02id\x18\x01 \x01(\x0b\x32 .cs3.sharing.ocm.v1beta1.ShareIdH\x00\x12\x30\n\x03key\x18\x02 \x01(\x0b\x32!.cs3.sharing.ocm.v1beta1.ShareKeyH\x00\x42\x06\n\x04spec\"\x84\x01\n\nShareGrant\x12\x36\n\x07grantee\x18\x01 \x01(\x0b\x32%.cs3.storage.provider.v1beta1.Grantee\x12>\n\x0bpermissions\x18\x02 \x01(\x0b\x32).cs3.sharing.ocm.v1beta1.SharePermissions\"b\n\x0cProviderInfo\x12\x0e\n\x06\x64omain\x18\x01 \x01(\t\x12\x13\n\x0b\x61pi_version\x18\x02 \x01(\t\x12\x14\n\x0c\x61pi_endpoint\x18\x03 \x01(\t\x12\x17\n\x0fwebdav_endpoint\x18\x04 \x01(\t*r\n\nShareState\x12\x17\n\x13SHARE_STATE_INVALID\x10\x00\x12\x17\n\x13SHARE_STATE_PENDING\x10\x01\x12\x18\n\x14SHARE_STATE_ACCEPTED\x10\x02\x12\x18\n\x14SHARE_STATE_REJECTED\x10\x03\x42u\n\x1b\x63om.cs3.sharing.ocm.v1beta1B\x0eResourcesProtoP\x01Z\nocmv1beta1\xa2\x02\x03\x43SO\xaa\x02\x17\x43s3.Sharing.Ocm.V1Beta1\xca\x02\x17\x43s3\\Sharing\\Ocm\\V1Beta1b\x06proto3')
  ,
  dependencies=[cs3_dot_identity_dot_user_dot_v1beta1_dot_resources__pb2.DESCRIPTOR,cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2.DESCRIPTOR,cs3_dot_types_dot_v1beta1_dot_types__pb2.DESCRIPTOR,])

_SHARESTATE = _descriptor.EnumDescriptor(
  name='ShareState',
  full_name='cs3.sharing.ocm.v1beta1.ShareState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SHARE_STATE_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHARE_STATE_PENDING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHARE_STATE_ACCEPTED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHARE_STATE_REJECTED', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1415,
  serialized_end=1529,
)
_sym_db.RegisterEnumDescriptor(_SHARESTATE)

ShareState = enum_type_wrapper.EnumTypeWrapper(_SHARESTATE)
SHARE_STATE_INVALID = 0
SHARE_STATE_PENDING = 1
SHARE_STATE_ACCEPTED = 2
SHARE_STATE_REJECTED = 3



_SHARE = _descriptor.Descriptor(
  name='Share',
  full_name='cs3.sharing.ocm.v1beta1.Share',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cs3.sharing.ocm.v1beta1.Share.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource_id', full_name='cs3.sharing.ocm.v1beta1.Share.resource_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permissions', full_name='cs3.sharing.ocm.v1beta1.Share.permissions', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grantee', full_name='cs3.sharing.ocm.v1beta1.Share.grantee', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='owner', full_name='cs3.sharing.ocm.v1beta1.Share.owner', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='cs3.sharing.ocm.v1beta1.Share.creator', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='cs3.sharing.ocm.v1beta1.Share.ctime', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='cs3.sharing.ocm.v1beta1.Share.mtime', index=7,
      number=8, type=11, cpp_type=10, label=1,
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
  serialized_start=189,
  serialized_end=617,
)


_SHAREPERMISSIONS = _descriptor.Descriptor(
  name='SharePermissions',
  full_name='cs3.sharing.ocm.v1beta1.SharePermissions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='permissions', full_name='cs3.sharing.ocm.v1beta1.SharePermissions.permissions', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reshare', full_name='cs3.sharing.ocm.v1beta1.SharePermissions.reshare', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=619,
  serialized_end=726,
)


_RECEIVEDSHARE = _descriptor.Descriptor(
  name='ReceivedShare',
  full_name='cs3.sharing.ocm.v1beta1.ReceivedShare',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='share', full_name='cs3.sharing.ocm.v1beta1.ReceivedShare.share', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='cs3.sharing.ocm.v1beta1.ReceivedShare.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=728,
  serialized_end=842,
)


_SHAREKEY = _descriptor.Descriptor(
  name='ShareKey',
  full_name='cs3.sharing.ocm.v1beta1.ShareKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='cs3.sharing.ocm.v1beta1.ShareKey.owner', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource_id', full_name='cs3.sharing.ocm.v1beta1.ShareKey.resource_id', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grantee', full_name='cs3.sharing.ocm.v1beta1.ShareKey.grantee', index=2,
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
  serialized_start=845,
  serialized_end=1024,
)


_SHAREID = _descriptor.Descriptor(
  name='ShareId',
  full_name='cs3.sharing.ocm.v1beta1.ShareId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opaque_id', full_name='cs3.sharing.ocm.v1beta1.ShareId.opaque_id', index=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1026,
  serialized_end=1054,
)


_SHAREREFERENCE = _descriptor.Descriptor(
  name='ShareReference',
  full_name='cs3.sharing.ocm.v1beta1.ShareReference',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cs3.sharing.ocm.v1beta1.ShareReference.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='cs3.sharing.ocm.v1beta1.ShareReference.key', index=1,
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
    _descriptor.OneofDescriptor(
      name='spec', full_name='cs3.sharing.ocm.v1beta1.ShareReference.spec',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1056,
  serialized_end=1178,
)


_SHAREGRANT = _descriptor.Descriptor(
  name='ShareGrant',
  full_name='cs3.sharing.ocm.v1beta1.ShareGrant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='grantee', full_name='cs3.sharing.ocm.v1beta1.ShareGrant.grantee', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permissions', full_name='cs3.sharing.ocm.v1beta1.ShareGrant.permissions', index=1,
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
  serialized_start=1181,
  serialized_end=1313,
)


_PROVIDERINFO = _descriptor.Descriptor(
  name='ProviderInfo',
  full_name='cs3.sharing.ocm.v1beta1.ProviderInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain', full_name='cs3.sharing.ocm.v1beta1.ProviderInfo.domain', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='api_version', full_name='cs3.sharing.ocm.v1beta1.ProviderInfo.api_version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='api_endpoint', full_name='cs3.sharing.ocm.v1beta1.ProviderInfo.api_endpoint', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='webdav_endpoint', full_name='cs3.sharing.ocm.v1beta1.ProviderInfo.webdav_endpoint', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1315,
  serialized_end=1413,
)

_SHARE.fields_by_name['id'].message_type = _SHAREID
_SHARE.fields_by_name['resource_id'].message_type = cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2._RESOURCEID
_SHARE.fields_by_name['permissions'].message_type = _SHAREPERMISSIONS
_SHARE.fields_by_name['grantee'].message_type = cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2._GRANTEE
_SHARE.fields_by_name['owner'].message_type = cs3_dot_identity_dot_user_dot_v1beta1_dot_resources__pb2._USERID
_SHARE.fields_by_name['creator'].message_type = cs3_dot_identity_dot_user_dot_v1beta1_dot_resources__pb2._USERID
_SHARE.fields_by_name['ctime'].message_type = cs3_dot_types_dot_v1beta1_dot_types__pb2._TIMESTAMP
_SHARE.fields_by_name['mtime'].message_type = cs3_dot_types_dot_v1beta1_dot_types__pb2._TIMESTAMP
_SHAREPERMISSIONS.fields_by_name['permissions'].message_type = cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2._RESOURCEPERMISSIONS
_RECEIVEDSHARE.fields_by_name['share'].message_type = _SHARE
_RECEIVEDSHARE.fields_by_name['state'].enum_type = _SHARESTATE
_SHAREKEY.fields_by_name['owner'].message_type = cs3_dot_identity_dot_user_dot_v1beta1_dot_resources__pb2._USERID
_SHAREKEY.fields_by_name['resource_id'].message_type = cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2._RESOURCEID
_SHAREKEY.fields_by_name['grantee'].message_type = cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2._GRANTEE
_SHAREREFERENCE.fields_by_name['id'].message_type = _SHAREID
_SHAREREFERENCE.fields_by_name['key'].message_type = _SHAREKEY
_SHAREREFERENCE.oneofs_by_name['spec'].fields.append(
  _SHAREREFERENCE.fields_by_name['id'])
_SHAREREFERENCE.fields_by_name['id'].containing_oneof = _SHAREREFERENCE.oneofs_by_name['spec']
_SHAREREFERENCE.oneofs_by_name['spec'].fields.append(
  _SHAREREFERENCE.fields_by_name['key'])
_SHAREREFERENCE.fields_by_name['key'].containing_oneof = _SHAREREFERENCE.oneofs_by_name['spec']
_SHAREGRANT.fields_by_name['grantee'].message_type = cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2._GRANTEE
_SHAREGRANT.fields_by_name['permissions'].message_type = _SHAREPERMISSIONS
DESCRIPTOR.message_types_by_name['Share'] = _SHARE
DESCRIPTOR.message_types_by_name['SharePermissions'] = _SHAREPERMISSIONS
DESCRIPTOR.message_types_by_name['ReceivedShare'] = _RECEIVEDSHARE
DESCRIPTOR.message_types_by_name['ShareKey'] = _SHAREKEY
DESCRIPTOR.message_types_by_name['ShareId'] = _SHAREID
DESCRIPTOR.message_types_by_name['ShareReference'] = _SHAREREFERENCE
DESCRIPTOR.message_types_by_name['ShareGrant'] = _SHAREGRANT
DESCRIPTOR.message_types_by_name['ProviderInfo'] = _PROVIDERINFO
DESCRIPTOR.enum_types_by_name['ShareState'] = _SHARESTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Share = _reflection.GeneratedProtocolMessageType('Share', (_message.Message,), {
  'DESCRIPTOR' : _SHARE,
  '__module__' : 'cs3.sharing.ocm.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.ocm.v1beta1.Share)
  })
_sym_db.RegisterMessage(Share)

SharePermissions = _reflection.GeneratedProtocolMessageType('SharePermissions', (_message.Message,), {
  'DESCRIPTOR' : _SHAREPERMISSIONS,
  '__module__' : 'cs3.sharing.ocm.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.ocm.v1beta1.SharePermissions)
  })
_sym_db.RegisterMessage(SharePermissions)

ReceivedShare = _reflection.GeneratedProtocolMessageType('ReceivedShare', (_message.Message,), {
  'DESCRIPTOR' : _RECEIVEDSHARE,
  '__module__' : 'cs3.sharing.ocm.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.ocm.v1beta1.ReceivedShare)
  })
_sym_db.RegisterMessage(ReceivedShare)

ShareKey = _reflection.GeneratedProtocolMessageType('ShareKey', (_message.Message,), {
  'DESCRIPTOR' : _SHAREKEY,
  '__module__' : 'cs3.sharing.ocm.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.ocm.v1beta1.ShareKey)
  })
_sym_db.RegisterMessage(ShareKey)

ShareId = _reflection.GeneratedProtocolMessageType('ShareId', (_message.Message,), {
  'DESCRIPTOR' : _SHAREID,
  '__module__' : 'cs3.sharing.ocm.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.ocm.v1beta1.ShareId)
  })
_sym_db.RegisterMessage(ShareId)

ShareReference = _reflection.GeneratedProtocolMessageType('ShareReference', (_message.Message,), {
  'DESCRIPTOR' : _SHAREREFERENCE,
  '__module__' : 'cs3.sharing.ocm.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.ocm.v1beta1.ShareReference)
  })
_sym_db.RegisterMessage(ShareReference)

ShareGrant = _reflection.GeneratedProtocolMessageType('ShareGrant', (_message.Message,), {
  'DESCRIPTOR' : _SHAREGRANT,
  '__module__' : 'cs3.sharing.ocm.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.ocm.v1beta1.ShareGrant)
  })
_sym_db.RegisterMessage(ShareGrant)

ProviderInfo = _reflection.GeneratedProtocolMessageType('ProviderInfo', (_message.Message,), {
  'DESCRIPTOR' : _PROVIDERINFO,
  '__module__' : 'cs3.sharing.ocm.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.ocm.v1beta1.ProviderInfo)
  })
_sym_db.RegisterMessage(ProviderInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
