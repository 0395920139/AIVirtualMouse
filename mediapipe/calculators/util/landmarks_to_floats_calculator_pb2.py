# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/util/landmarks_to_floats_calculator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/calculators/util/landmarks_to_floats_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\n?mediapipe/calculators/util/landmarks_to_floats_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\x9d\x01\n\"LandmarksToFloatsCalculatorOptions\x12\x19\n\x0enum_dimensions\x18\x01 \x01(\x05:\x01\x32\x32\\\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xcc\xe7\xd5\x82\x01 \x01(\x0b\x32-.mediapipe.LandmarksToFloatsCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LANDMARKSTOFLOATSCALCULATOROPTIONS = _descriptor.Descriptor(
  name='LandmarksToFloatsCalculatorOptions',
  full_name='mediapipe.LandmarksToFloatsCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_dimensions', full_name='mediapipe.LandmarksToFloatsCalculatorOptions.num_dimensions', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.LandmarksToFloatsCalculatorOptions.ext', index=0,
      number=274035660, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=274,
)

DESCRIPTOR.message_types_by_name['LandmarksToFloatsCalculatorOptions'] = _LANDMARKSTOFLOATSCALCULATOROPTIONS

LandmarksToFloatsCalculatorOptions = _reflection.GeneratedProtocolMessageType('LandmarksToFloatsCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _LANDMARKSTOFLOATSCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.util.landmarks_to_floats_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.LandmarksToFloatsCalculatorOptions)
  ))
_sym_db.RegisterMessage(LandmarksToFloatsCalculatorOptions)

_LANDMARKSTOFLOATSCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _LANDMARKSTOFLOATSCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_LANDMARKSTOFLOATSCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
