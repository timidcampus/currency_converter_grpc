# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: currency_converter.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x63urrency_converter.proto\x12\x11\x63urrencyconverter\"d\n\x11\x43onversionRequest\x12\x0f\n\x07\x61pi_key\x18\x01 \x01(\t\x12\x15\n\rbase_currency\x18\x02 \x01(\t\x12\x17\n\x0ftarget_currency\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x01\"!\n\x10\x43onversionResult\x12\r\n\x05value\x18\x01 \x01(\x01\x32k\n\x11\x43urrencyConverter\x12V\n\x07\x43onvert\x12$.currencyconverter.ConversionRequest\x1a#.currencyconverter.ConversionResult\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'currency_converter_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONVERSIONREQUEST._serialized_start=47
  _CONVERSIONREQUEST._serialized_end=147
  _CONVERSIONRESULT._serialized_start=149
  _CONVERSIONRESULT._serialized_end=182
  _CURRENCYCONVERTER._serialized_start=184
  _CURRENCYCONVERTER._serialized_end=291
# @@protoc_insertion_point(module_scope)