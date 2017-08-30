# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: device.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='device.proto',
  package='google.internal.devtools.workerfarm.v1test1',
  syntax='proto3',
  serialized_pb=_b('\n\x0c\x64\x65vice.proto\x12+google.internal.devtools.workerfarm.v1test1\"\xd2\x02\n\rPrimaryDevice\x12O\n\nproperties\x18\x01 \x03(\x0b\x32;.google.internal.devtools.workerfarm.v1test1.DeviceProperty\x12N\n\tresources\x18\x02 \x03(\x0b\x32;.google.internal.devtools.workerfarm.v1test1.DeviceResource\x12L\n\x07\x64\x65vices\x18\x03 \x03(\x0b\x32;.google.internal.devtools.workerfarm.v1test1.AttachedDevice\x12R\n\x0b\x63onnections\x18\x04 \x03(\x0b\x32=.google.internal.devtools.workerfarm.v1test1.DeviceConnection\"d\n\x0e\x44\x65viceProperty\x12\x43\n\x03key\x18\x01 \x01(\x0b\x32\x36.google.internal.devtools.workerfarm.v1test1.DeviceKey\x12\r\n\x05value\x18\x02 \x01(\t\"d\n\x0e\x44\x65viceResource\x12\x43\n\x03key\x18\x01 \x01(\x0b\x32\x36.google.internal.devtools.workerfarm.v1test1.DeviceKey\x12\r\n\x05value\x18\x02 \x01(\x02\"\xbf\x01\n\x0e\x41ttachedDevice\x12\x0c\n\x04name\x18\x01 \x01(\t\x12O\n\nproperties\x18\x02 \x03(\x0b\x32;.google.internal.devtools.workerfarm.v1test1.DeviceProperty\x12N\n\tresources\x18\x03 \x03(\x0b\x32;.google.internal.devtools.workerfarm.v1test1.DeviceResource\"b\n\x10\x44\x65viceConnection\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06source\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x03 \x01(\t\x12\x1b\n\x13\x64\x65stination_address\x18\x04 \x01(\t\"9\n\tDeviceKey\x12\x12\n\x08standard\x18\x01 \x01(\x05H\x00\x12\x10\n\x06\x63ustom\x18\x02 \x01(\tH\x00\x42\x06\n\x04typeb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PRIMARYDEVICE = _descriptor.Descriptor(
  name='PrimaryDevice',
  full_name='google.internal.devtools.workerfarm.v1test1.PrimaryDevice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='properties', full_name='google.internal.devtools.workerfarm.v1test1.PrimaryDevice.properties', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resources', full_name='google.internal.devtools.workerfarm.v1test1.PrimaryDevice.resources', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='devices', full_name='google.internal.devtools.workerfarm.v1test1.PrimaryDevice.devices', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='connections', full_name='google.internal.devtools.workerfarm.v1test1.PrimaryDevice.connections', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=400,
)


_DEVICEPROPERTY = _descriptor.Descriptor(
  name='DeviceProperty',
  full_name='google.internal.devtools.workerfarm.v1test1.DeviceProperty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.internal.devtools.workerfarm.v1test1.DeviceProperty.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.internal.devtools.workerfarm.v1test1.DeviceProperty.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=402,
  serialized_end=502,
)


_DEVICERESOURCE = _descriptor.Descriptor(
  name='DeviceResource',
  full_name='google.internal.devtools.workerfarm.v1test1.DeviceResource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.internal.devtools.workerfarm.v1test1.DeviceResource.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.internal.devtools.workerfarm.v1test1.DeviceResource.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=504,
  serialized_end=604,
)


_ATTACHEDDEVICE = _descriptor.Descriptor(
  name='AttachedDevice',
  full_name='google.internal.devtools.workerfarm.v1test1.AttachedDevice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.internal.devtools.workerfarm.v1test1.AttachedDevice.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='properties', full_name='google.internal.devtools.workerfarm.v1test1.AttachedDevice.properties', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resources', full_name='google.internal.devtools.workerfarm.v1test1.AttachedDevice.resources', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=607,
  serialized_end=798,
)


_DEVICECONNECTION = _descriptor.Descriptor(
  name='DeviceConnection',
  full_name='google.internal.devtools.workerfarm.v1test1.DeviceConnection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='google.internal.devtools.workerfarm.v1test1.DeviceConnection.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='google.internal.devtools.workerfarm.v1test1.DeviceConnection.source', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='destination', full_name='google.internal.devtools.workerfarm.v1test1.DeviceConnection.destination', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='destination_address', full_name='google.internal.devtools.workerfarm.v1test1.DeviceConnection.destination_address', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=800,
  serialized_end=898,
)


_DEVICEKEY = _descriptor.Descriptor(
  name='DeviceKey',
  full_name='google.internal.devtools.workerfarm.v1test1.DeviceKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='standard', full_name='google.internal.devtools.workerfarm.v1test1.DeviceKey.standard', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='custom', full_name='google.internal.devtools.workerfarm.v1test1.DeviceKey.custom', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='type', full_name='google.internal.devtools.workerfarm.v1test1.DeviceKey.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=900,
  serialized_end=957,
)

_PRIMARYDEVICE.fields_by_name['properties'].message_type = _DEVICEPROPERTY
_PRIMARYDEVICE.fields_by_name['resources'].message_type = _DEVICERESOURCE
_PRIMARYDEVICE.fields_by_name['devices'].message_type = _ATTACHEDDEVICE
_PRIMARYDEVICE.fields_by_name['connections'].message_type = _DEVICECONNECTION
_DEVICEPROPERTY.fields_by_name['key'].message_type = _DEVICEKEY
_DEVICERESOURCE.fields_by_name['key'].message_type = _DEVICEKEY
_ATTACHEDDEVICE.fields_by_name['properties'].message_type = _DEVICEPROPERTY
_ATTACHEDDEVICE.fields_by_name['resources'].message_type = _DEVICERESOURCE
_DEVICEKEY.oneofs_by_name['type'].fields.append(
  _DEVICEKEY.fields_by_name['standard'])
_DEVICEKEY.fields_by_name['standard'].containing_oneof = _DEVICEKEY.oneofs_by_name['type']
_DEVICEKEY.oneofs_by_name['type'].fields.append(
  _DEVICEKEY.fields_by_name['custom'])
_DEVICEKEY.fields_by_name['custom'].containing_oneof = _DEVICEKEY.oneofs_by_name['type']
DESCRIPTOR.message_types_by_name['PrimaryDevice'] = _PRIMARYDEVICE
DESCRIPTOR.message_types_by_name['DeviceProperty'] = _DEVICEPROPERTY
DESCRIPTOR.message_types_by_name['DeviceResource'] = _DEVICERESOURCE
DESCRIPTOR.message_types_by_name['AttachedDevice'] = _ATTACHEDDEVICE
DESCRIPTOR.message_types_by_name['DeviceConnection'] = _DEVICECONNECTION
DESCRIPTOR.message_types_by_name['DeviceKey'] = _DEVICEKEY

PrimaryDevice = _reflection.GeneratedProtocolMessageType('PrimaryDevice', (_message.Message,), dict(
  DESCRIPTOR = _PRIMARYDEVICE,
  __module__ = 'device_pb2'
  # @@protoc_insertion_point(class_scope:google.internal.devtools.workerfarm.v1test1.PrimaryDevice)
  ))
_sym_db.RegisterMessage(PrimaryDevice)

DeviceProperty = _reflection.GeneratedProtocolMessageType('DeviceProperty', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEPROPERTY,
  __module__ = 'device_pb2'
  # @@protoc_insertion_point(class_scope:google.internal.devtools.workerfarm.v1test1.DeviceProperty)
  ))
_sym_db.RegisterMessage(DeviceProperty)

DeviceResource = _reflection.GeneratedProtocolMessageType('DeviceResource', (_message.Message,), dict(
  DESCRIPTOR = _DEVICERESOURCE,
  __module__ = 'device_pb2'
  # @@protoc_insertion_point(class_scope:google.internal.devtools.workerfarm.v1test1.DeviceResource)
  ))
_sym_db.RegisterMessage(DeviceResource)

AttachedDevice = _reflection.GeneratedProtocolMessageType('AttachedDevice', (_message.Message,), dict(
  DESCRIPTOR = _ATTACHEDDEVICE,
  __module__ = 'device_pb2'
  # @@protoc_insertion_point(class_scope:google.internal.devtools.workerfarm.v1test1.AttachedDevice)
  ))
_sym_db.RegisterMessage(AttachedDevice)

DeviceConnection = _reflection.GeneratedProtocolMessageType('DeviceConnection', (_message.Message,), dict(
  DESCRIPTOR = _DEVICECONNECTION,
  __module__ = 'device_pb2'
  # @@protoc_insertion_point(class_scope:google.internal.devtools.workerfarm.v1test1.DeviceConnection)
  ))
_sym_db.RegisterMessage(DeviceConnection)

DeviceKey = _reflection.GeneratedProtocolMessageType('DeviceKey', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEKEY,
  __module__ = 'device_pb2'
  # @@protoc_insertion_point(class_scope:google.internal.devtools.workerfarm.v1test1.DeviceKey)
  ))
_sym_db.RegisterMessage(DeviceKey)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)