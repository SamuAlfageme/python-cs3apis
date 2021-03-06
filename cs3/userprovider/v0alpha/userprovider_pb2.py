# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/userprovider/v0alpha/userprovider.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.rpc import status_pb2 as cs3_dot_rpc_dot_status__pb2
from cs3.types import types_pb2 as cs3_dot_types_dot_types__pb2
from cs3.userprovider.v0alpha import resources_pb2 as cs3_dot_userprovider_dot_v0alpha_dot_resources__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cs3/userprovider/v0alpha/userprovider.proto',
  package='cs3.userproviderv0alpha',
  syntax='proto3',
  serialized_options=_b('\n\033com.cs3.userproviderv0alphaB\021UserproviderProtoP\001Z\025userproviderv0alphapb\242\002\020CBOXUSERPROVIDER\252\002\027CS3.UserProviderV0Alpha\312\002\027CS3\\UserProviderV0Alpha'),
  serialized_pb=_b('\n+cs3/userprovider/v0alpha/userprovider.proto\x12\x17\x63s3.userproviderv0alpha\x1a\x14\x63s3/rpc/status.proto\x1a\x15\x63s3/types/types.proto\x1a(cs3/userprovider/v0alpha/resources.proto\"W\n\x0eGetUserRequest\x12!\n\x06opaque\x18\x01 \x01(\x0b\x32\x11.cs3.types.Opaque\x12\"\n\x07user_id\x18\x02 \x01(\x0b\x32\x11.cs3.types.UserId\"\x82\x01\n\x0fGetUserResponse\x12\x1f\n\x06status\x18\x01 \x01(\x0b\x32\x0f.cs3.rpc.Status\x12!\n\x06opaque\x18\x02 \x01(\x0b\x32\x11.cs3.types.Opaque\x12+\n\x04user\x18\x03 \x01(\x0b\x32\x1d.cs3.userproviderv0alpha.User\"]\n\x14GetUserGroupsRequest\x12!\n\x06opaque\x18\x01 \x01(\x0b\x32\x11.cs3.types.Opaque\x12\"\n\x07user_id\x18\x02 \x01(\x0b\x32\x11.cs3.types.UserId\"k\n\x15GetUserGroupsResponse\x12\x1f\n\x06status\x18\x01 \x01(\x0b\x32\x0f.cs3.rpc.Status\x12!\n\x06opaque\x18\x02 \x01(\x0b\x32\x11.cs3.types.Opaque\x12\x0e\n\x06groups\x18\x03 \x03(\t\"h\n\x10IsInGroupRequest\x12!\n\x06opaque\x18\x01 \x01(\x0b\x32\x11.cs3.types.Opaque\x12\"\n\x07user_id\x18\x02 \x01(\x0b\x32\x11.cs3.types.UserId\x12\r\n\x05group\x18\x03 \x01(\t\"c\n\x11IsInGroupResponse\x12\x1f\n\x06status\x18\x01 \x01(\x0b\x32\x0f.cs3.rpc.Status\x12!\n\x06opaque\x18\x02 \x01(\x0b\x32\x11.cs3.types.Opaque\x12\n\n\x02ok\x18\x03 \x01(\x08\"E\n\x10\x46indUsersRequest\x12!\n\x06opaque\x18\x01 \x01(\x0b\x32\x11.cs3.types.Opaque\x12\x0e\n\x06\x66ilter\x18\x02 \x01(\t\"\x85\x01\n\x11\x46indUsersResponse\x12\x1f\n\x06status\x18\x01 \x01(\x0b\x32\x0f.cs3.rpc.Status\x12!\n\x06opaque\x18\x02 \x01(\x0b\x32\x11.cs3.types.Opaque\x12,\n\x05users\x18\x03 \x03(\x0b\x32\x1d.cs3.userproviderv0alpha.User2\xab\x03\n\x13UserProviderService\x12\\\n\x07GetUser\x12\'.cs3.userproviderv0alpha.GetUserRequest\x1a(.cs3.userproviderv0alpha.GetUserResponse\x12n\n\rGetUserGroups\x12-.cs3.userproviderv0alpha.GetUserGroupsRequest\x1a..cs3.userproviderv0alpha.GetUserGroupsResponse\x12\x62\n\tIsInGroup\x12).cs3.userproviderv0alpha.IsInGroupRequest\x1a*.cs3.userproviderv0alpha.IsInGroupResponse\x12\x62\n\tFindUsers\x12).cs3.userproviderv0alpha.FindUsersRequest\x1a*.cs3.userproviderv0alpha.FindUsersResponseB\x90\x01\n\x1b\x63om.cs3.userproviderv0alphaB\x11UserproviderProtoP\x01Z\x15userproviderv0alphapb\xa2\x02\x10\x43\x42OXUSERPROVIDER\xaa\x02\x17\x43S3.UserProviderV0Alpha\xca\x02\x17\x43S3\\UserProviderV0Alphab\x06proto3')
  ,
  dependencies=[cs3_dot_rpc_dot_status__pb2.DESCRIPTOR,cs3_dot_types_dot_types__pb2.DESCRIPTOR,cs3_dot_userprovider_dot_v0alpha_dot_resources__pb2.DESCRIPTOR,])




_GETUSERREQUEST = _descriptor.Descriptor(
  name='GetUserRequest',
  full_name='cs3.userproviderv0alpha.GetUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.userproviderv0alpha.GetUserRequest.opaque', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='cs3.userproviderv0alpha.GetUserRequest.user_id', index=1,
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
  serialized_start=159,
  serialized_end=246,
)


_GETUSERRESPONSE = _descriptor.Descriptor(
  name='GetUserResponse',
  full_name='cs3.userproviderv0alpha.GetUserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cs3.userproviderv0alpha.GetUserResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.userproviderv0alpha.GetUserResponse.opaque', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='cs3.userproviderv0alpha.GetUserResponse.user', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=249,
  serialized_end=379,
)


_GETUSERGROUPSREQUEST = _descriptor.Descriptor(
  name='GetUserGroupsRequest',
  full_name='cs3.userproviderv0alpha.GetUserGroupsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.userproviderv0alpha.GetUserGroupsRequest.opaque', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='cs3.userproviderv0alpha.GetUserGroupsRequest.user_id', index=1,
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
  serialized_start=381,
  serialized_end=474,
)


_GETUSERGROUPSRESPONSE = _descriptor.Descriptor(
  name='GetUserGroupsResponse',
  full_name='cs3.userproviderv0alpha.GetUserGroupsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cs3.userproviderv0alpha.GetUserGroupsResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.userproviderv0alpha.GetUserGroupsResponse.opaque', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='groups', full_name='cs3.userproviderv0alpha.GetUserGroupsResponse.groups', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=476,
  serialized_end=583,
)


_ISINGROUPREQUEST = _descriptor.Descriptor(
  name='IsInGroupRequest',
  full_name='cs3.userproviderv0alpha.IsInGroupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.userproviderv0alpha.IsInGroupRequest.opaque', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='cs3.userproviderv0alpha.IsInGroupRequest.user_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group', full_name='cs3.userproviderv0alpha.IsInGroupRequest.group', index=2,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=585,
  serialized_end=689,
)


_ISINGROUPRESPONSE = _descriptor.Descriptor(
  name='IsInGroupResponse',
  full_name='cs3.userproviderv0alpha.IsInGroupResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cs3.userproviderv0alpha.IsInGroupResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.userproviderv0alpha.IsInGroupResponse.opaque', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ok', full_name='cs3.userproviderv0alpha.IsInGroupResponse.ok', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=691,
  serialized_end=790,
)


_FINDUSERSREQUEST = _descriptor.Descriptor(
  name='FindUsersRequest',
  full_name='cs3.userproviderv0alpha.FindUsersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.userproviderv0alpha.FindUsersRequest.opaque', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='cs3.userproviderv0alpha.FindUsersRequest.filter', index=1,
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
  serialized_start=792,
  serialized_end=861,
)


_FINDUSERSRESPONSE = _descriptor.Descriptor(
  name='FindUsersResponse',
  full_name='cs3.userproviderv0alpha.FindUsersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cs3.userproviderv0alpha.FindUsersResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.userproviderv0alpha.FindUsersResponse.opaque', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='users', full_name='cs3.userproviderv0alpha.FindUsersResponse.users', index=2,
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
  serialized_start=864,
  serialized_end=997,
)

_GETUSERREQUEST.fields_by_name['opaque'].message_type = cs3_dot_types_dot_types__pb2._OPAQUE
_GETUSERREQUEST.fields_by_name['user_id'].message_type = cs3_dot_types_dot_types__pb2._USERID
_GETUSERRESPONSE.fields_by_name['status'].message_type = cs3_dot_rpc_dot_status__pb2._STATUS
_GETUSERRESPONSE.fields_by_name['opaque'].message_type = cs3_dot_types_dot_types__pb2._OPAQUE
_GETUSERRESPONSE.fields_by_name['user'].message_type = cs3_dot_userprovider_dot_v0alpha_dot_resources__pb2._USER
_GETUSERGROUPSREQUEST.fields_by_name['opaque'].message_type = cs3_dot_types_dot_types__pb2._OPAQUE
_GETUSERGROUPSREQUEST.fields_by_name['user_id'].message_type = cs3_dot_types_dot_types__pb2._USERID
_GETUSERGROUPSRESPONSE.fields_by_name['status'].message_type = cs3_dot_rpc_dot_status__pb2._STATUS
_GETUSERGROUPSRESPONSE.fields_by_name['opaque'].message_type = cs3_dot_types_dot_types__pb2._OPAQUE
_ISINGROUPREQUEST.fields_by_name['opaque'].message_type = cs3_dot_types_dot_types__pb2._OPAQUE
_ISINGROUPREQUEST.fields_by_name['user_id'].message_type = cs3_dot_types_dot_types__pb2._USERID
_ISINGROUPRESPONSE.fields_by_name['status'].message_type = cs3_dot_rpc_dot_status__pb2._STATUS
_ISINGROUPRESPONSE.fields_by_name['opaque'].message_type = cs3_dot_types_dot_types__pb2._OPAQUE
_FINDUSERSREQUEST.fields_by_name['opaque'].message_type = cs3_dot_types_dot_types__pb2._OPAQUE
_FINDUSERSRESPONSE.fields_by_name['status'].message_type = cs3_dot_rpc_dot_status__pb2._STATUS
_FINDUSERSRESPONSE.fields_by_name['opaque'].message_type = cs3_dot_types_dot_types__pb2._OPAQUE
_FINDUSERSRESPONSE.fields_by_name['users'].message_type = cs3_dot_userprovider_dot_v0alpha_dot_resources__pb2._USER
DESCRIPTOR.message_types_by_name['GetUserRequest'] = _GETUSERREQUEST
DESCRIPTOR.message_types_by_name['GetUserResponse'] = _GETUSERRESPONSE
DESCRIPTOR.message_types_by_name['GetUserGroupsRequest'] = _GETUSERGROUPSREQUEST
DESCRIPTOR.message_types_by_name['GetUserGroupsResponse'] = _GETUSERGROUPSRESPONSE
DESCRIPTOR.message_types_by_name['IsInGroupRequest'] = _ISINGROUPREQUEST
DESCRIPTOR.message_types_by_name['IsInGroupResponse'] = _ISINGROUPRESPONSE
DESCRIPTOR.message_types_by_name['FindUsersRequest'] = _FINDUSERSREQUEST
DESCRIPTOR.message_types_by_name['FindUsersResponse'] = _FINDUSERSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetUserRequest = _reflection.GeneratedProtocolMessageType('GetUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERREQUEST,
  '__module__' : 'cs3.userprovider.v0alpha.userprovider_pb2'
  # @@protoc_insertion_point(class_scope:cs3.userproviderv0alpha.GetUserRequest)
  })
_sym_db.RegisterMessage(GetUserRequest)

GetUserResponse = _reflection.GeneratedProtocolMessageType('GetUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERRESPONSE,
  '__module__' : 'cs3.userprovider.v0alpha.userprovider_pb2'
  # @@protoc_insertion_point(class_scope:cs3.userproviderv0alpha.GetUserResponse)
  })
_sym_db.RegisterMessage(GetUserResponse)

GetUserGroupsRequest = _reflection.GeneratedProtocolMessageType('GetUserGroupsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERGROUPSREQUEST,
  '__module__' : 'cs3.userprovider.v0alpha.userprovider_pb2'
  # @@protoc_insertion_point(class_scope:cs3.userproviderv0alpha.GetUserGroupsRequest)
  })
_sym_db.RegisterMessage(GetUserGroupsRequest)

GetUserGroupsResponse = _reflection.GeneratedProtocolMessageType('GetUserGroupsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERGROUPSRESPONSE,
  '__module__' : 'cs3.userprovider.v0alpha.userprovider_pb2'
  # @@protoc_insertion_point(class_scope:cs3.userproviderv0alpha.GetUserGroupsResponse)
  })
_sym_db.RegisterMessage(GetUserGroupsResponse)

IsInGroupRequest = _reflection.GeneratedProtocolMessageType('IsInGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _ISINGROUPREQUEST,
  '__module__' : 'cs3.userprovider.v0alpha.userprovider_pb2'
  # @@protoc_insertion_point(class_scope:cs3.userproviderv0alpha.IsInGroupRequest)
  })
_sym_db.RegisterMessage(IsInGroupRequest)

IsInGroupResponse = _reflection.GeneratedProtocolMessageType('IsInGroupResponse', (_message.Message,), {
  'DESCRIPTOR' : _ISINGROUPRESPONSE,
  '__module__' : 'cs3.userprovider.v0alpha.userprovider_pb2'
  # @@protoc_insertion_point(class_scope:cs3.userproviderv0alpha.IsInGroupResponse)
  })
_sym_db.RegisterMessage(IsInGroupResponse)

FindUsersRequest = _reflection.GeneratedProtocolMessageType('FindUsersRequest', (_message.Message,), {
  'DESCRIPTOR' : _FINDUSERSREQUEST,
  '__module__' : 'cs3.userprovider.v0alpha.userprovider_pb2'
  # @@protoc_insertion_point(class_scope:cs3.userproviderv0alpha.FindUsersRequest)
  })
_sym_db.RegisterMessage(FindUsersRequest)

FindUsersResponse = _reflection.GeneratedProtocolMessageType('FindUsersResponse', (_message.Message,), {
  'DESCRIPTOR' : _FINDUSERSRESPONSE,
  '__module__' : 'cs3.userprovider.v0alpha.userprovider_pb2'
  # @@protoc_insertion_point(class_scope:cs3.userproviderv0alpha.FindUsersResponse)
  })
_sym_db.RegisterMessage(FindUsersResponse)


DESCRIPTOR._options = None

_USERPROVIDERSERVICE = _descriptor.ServiceDescriptor(
  name='UserProviderService',
  full_name='cs3.userproviderv0alpha.UserProviderService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1000,
  serialized_end=1427,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetUser',
    full_name='cs3.userproviderv0alpha.UserProviderService.GetUser',
    index=0,
    containing_service=None,
    input_type=_GETUSERREQUEST,
    output_type=_GETUSERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetUserGroups',
    full_name='cs3.userproviderv0alpha.UserProviderService.GetUserGroups',
    index=1,
    containing_service=None,
    input_type=_GETUSERGROUPSREQUEST,
    output_type=_GETUSERGROUPSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='IsInGroup',
    full_name='cs3.userproviderv0alpha.UserProviderService.IsInGroup',
    index=2,
    containing_service=None,
    input_type=_ISINGROUPREQUEST,
    output_type=_ISINGROUPRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FindUsers',
    full_name='cs3.userproviderv0alpha.UserProviderService.FindUsers',
    index=3,
    containing_service=None,
    input_type=_FINDUSERSREQUEST,
    output_type=_FINDUSERSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERPROVIDERSERVICE)

DESCRIPTOR.services_by_name['UserProviderService'] = _USERPROVIDERSERVICE

# @@protoc_insertion_point(module_scope)
