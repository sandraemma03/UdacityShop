# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: demo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='demo.proto',
  package='hipstershop',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ndemo.proto\x12\x0bhipstershop\"\x07\n\x05\x45mpty\"\x84\x01\n\x07Product\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0f\n\x07picture\x18\x04 \x01(\t\x12%\n\tprice_usd\x18\x05 \x01(\x0b\x32\x12.hipstershop.Money\x12\x12\n\ncategories\x18\x06 \x03(\t\">\n\x14ListProductsResponse\x12&\n\x08products\x18\x01 \x03(\x0b\x32\x14.hipstershop.Product\"\x1f\n\x11GetProductRequest\x12\n\n\x02id\x18\x01 \x01(\t\"&\n\x15SearchProductsRequest\x12\r\n\x05query\x18\x01 \x01(\t\"?\n\x16SearchProductsResponse\x12%\n\x07results\x18\x01 \x03(\x0b\x32\x14.hipstershop.Product\"<\n\x05Money\x12\x15\n\rcurrency_code\x18\x01 \x01(\t\x12\r\n\x05units\x18\x02 \x01(\x03\x12\r\n\x05nanos\x18\x03 \x01(\x05\"8\n\x1eGetSupportedCurrenciesResponse\x12\x16\n\x0e\x63urrency_codes\x18\x01 \x03(\t\"N\n\x19\x43urrencyConversionRequest\x12 \n\x04\x66rom\x18\x01 \x01(\x0b\x32\x12.hipstershop.Money\x12\x0f\n\x07to_code\x18\x02 \x01(\t\"!\n\tAdRequest\x12\x14\n\x0c\x63ontext_keys\x18\x01 \x03(\t\"*\n\nAdResponse\x12\x1c\n\x03\x61\x64s\x18\x01 \x03(\x0b\x32\x0f.hipstershop.Ad\"(\n\x02\x41\x64\x12\x14\n\x0credirect_url\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t2\x83\x02\n\x15ProductCatalogService\x12G\n\x0cListProducts\x12\x12.hipstershop.Empty\x1a!.hipstershop.ListProductsResponse\"\x00\x12\x44\n\nGetProduct\x12\x1e.hipstershop.GetProductRequest\x1a\x14.hipstershop.Product\"\x00\x12[\n\x0eSearchProducts\x12\".hipstershop.SearchProductsRequest\x1a#.hipstershop.SearchProductsResponse\"\x00\x32\xb7\x01\n\x0f\x43urrencyService\x12[\n\x16GetSupportedCurrencies\x12\x12.hipstershop.Empty\x1a+.hipstershop.GetSupportedCurrenciesResponse\"\x00\x12G\n\x07\x43onvert\x12&.hipstershop.CurrencyConversionRequest\x1a\x12.hipstershop.Money\"\x00\x32H\n\tAdService\x12;\n\x06GetAds\x12\x16.hipstershop.AdRequest\x1a\x17.hipstershop.AdResponse\"\x00\x32J\n\x0b\x41\x64ServiceV2\x12;\n\x06GetAds\x12\x16.hipstershop.AdRequest\x1a\x17.hipstershop.AdResponse\"\x00\x62\x06proto3'
)




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='hipstershop.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=27,
  serialized_end=34,
)


_PRODUCT = _descriptor.Descriptor(
  name='Product',
  full_name='hipstershop.Product',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='hipstershop.Product.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='hipstershop.Product.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='hipstershop.Product.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='picture', full_name='hipstershop.Product.picture', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price_usd', full_name='hipstershop.Product.price_usd', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='categories', full_name='hipstershop.Product.categories', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=37,
  serialized_end=169,
)


_LISTPRODUCTSRESPONSE = _descriptor.Descriptor(
  name='ListProductsResponse',
  full_name='hipstershop.ListProductsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='products', full_name='hipstershop.ListProductsResponse.products', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=171,
  serialized_end=233,
)


_GETPRODUCTREQUEST = _descriptor.Descriptor(
  name='GetProductRequest',
  full_name='hipstershop.GetProductRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='hipstershop.GetProductRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=235,
  serialized_end=266,
)


_SEARCHPRODUCTSREQUEST = _descriptor.Descriptor(
  name='SearchProductsRequest',
  full_name='hipstershop.SearchProductsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='hipstershop.SearchProductsRequest.query', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=268,
  serialized_end=306,
)


_SEARCHPRODUCTSRESPONSE = _descriptor.Descriptor(
  name='SearchProductsResponse',
  full_name='hipstershop.SearchProductsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='hipstershop.SearchProductsResponse.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=308,
  serialized_end=371,
)


_MONEY = _descriptor.Descriptor(
  name='Money',
  full_name='hipstershop.Money',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='currency_code', full_name='hipstershop.Money.currency_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='units', full_name='hipstershop.Money.units', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nanos', full_name='hipstershop.Money.nanos', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=373,
  serialized_end=433,
)


_GETSUPPORTEDCURRENCIESRESPONSE = _descriptor.Descriptor(
  name='GetSupportedCurrenciesResponse',
  full_name='hipstershop.GetSupportedCurrenciesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='currency_codes', full_name='hipstershop.GetSupportedCurrenciesResponse.currency_codes', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=435,
  serialized_end=491,
)


_CURRENCYCONVERSIONREQUEST = _descriptor.Descriptor(
  name='CurrencyConversionRequest',
  full_name='hipstershop.CurrencyConversionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='from', full_name='hipstershop.CurrencyConversionRequest.from', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to_code', full_name='hipstershop.CurrencyConversionRequest.to_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=493,
  serialized_end=571,
)


_ADREQUEST = _descriptor.Descriptor(
  name='AdRequest',
  full_name='hipstershop.AdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='context_keys', full_name='hipstershop.AdRequest.context_keys', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=573,
  serialized_end=606,
)


_ADRESPONSE = _descriptor.Descriptor(
  name='AdResponse',
  full_name='hipstershop.AdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ads', full_name='hipstershop.AdResponse.ads', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=608,
  serialized_end=650,
)


_AD = _descriptor.Descriptor(
  name='Ad',
  full_name='hipstershop.Ad',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='redirect_url', full_name='hipstershop.Ad.redirect_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='hipstershop.Ad.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=652,
  serialized_end=692,
)

_PRODUCT.fields_by_name['price_usd'].message_type = _MONEY
_LISTPRODUCTSRESPONSE.fields_by_name['products'].message_type = _PRODUCT
_SEARCHPRODUCTSRESPONSE.fields_by_name['results'].message_type = _PRODUCT
_CURRENCYCONVERSIONREQUEST.fields_by_name['from'].message_type = _MONEY
_ADRESPONSE.fields_by_name['ads'].message_type = _AD
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['Product'] = _PRODUCT
DESCRIPTOR.message_types_by_name['ListProductsResponse'] = _LISTPRODUCTSRESPONSE
DESCRIPTOR.message_types_by_name['GetProductRequest'] = _GETPRODUCTREQUEST
DESCRIPTOR.message_types_by_name['SearchProductsRequest'] = _SEARCHPRODUCTSREQUEST
DESCRIPTOR.message_types_by_name['SearchProductsResponse'] = _SEARCHPRODUCTSRESPONSE
DESCRIPTOR.message_types_by_name['Money'] = _MONEY
DESCRIPTOR.message_types_by_name['GetSupportedCurrenciesResponse'] = _GETSUPPORTEDCURRENCIESRESPONSE
DESCRIPTOR.message_types_by_name['CurrencyConversionRequest'] = _CURRENCYCONVERSIONREQUEST
DESCRIPTOR.message_types_by_name['AdRequest'] = _ADREQUEST
DESCRIPTOR.message_types_by_name['AdResponse'] = _ADRESPONSE
DESCRIPTOR.message_types_by_name['Ad'] = _AD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.Empty)
  })
_sym_db.RegisterMessage(Empty)

Product = _reflection.GeneratedProtocolMessageType('Product', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCT,
  '__module__' : 'demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.Product)
  })
_sym_db.RegisterMessage(Product)

ListProductsResponse = _reflection.GeneratedProtocolMessageType('ListProductsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTPRODUCTSRESPONSE,
  '__module__' : 'demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.ListProductsResponse)
  })
_sym_db.RegisterMessage(ListProductsResponse)

GetProductRequest = _reflection.GeneratedProtocolMessageType('GetProductRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPRODUCTREQUEST,
  '__module__' : 'demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.GetProductRequest)
  })
_sym_db.RegisterMessage(GetProductRequest)

SearchProductsRequest = _reflection.GeneratedProtocolMessageType('SearchProductsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHPRODUCTSREQUEST,
  '__module__' : 'demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.SearchProductsRequest)
  })
_sym_db.RegisterMessage(SearchProductsRequest)

SearchProductsResponse = _reflection.GeneratedProtocolMessageType('SearchProductsResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHPRODUCTSRESPONSE,
  '__module__' : 'demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.SearchProductsResponse)
  })
_sym_db.RegisterMessage(SearchProductsResponse)

Money = _reflection.GeneratedProtocolMessageType('Money', (_message.Message,), {
  'DESCRIPTOR' : _MONEY,
  '__module__' : 'demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.Money)
  })
_sym_db.RegisterMessage(Money)

GetSupportedCurrenciesResponse = _reflection.GeneratedProtocolMessageType('GetSupportedCurrenciesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSUPPORTEDCURRENCIESRESPONSE,
  '__module__' : 'demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.GetSupportedCurrenciesResponse)
  })
_sym_db.RegisterMessage(GetSupportedCurrenciesResponse)

CurrencyConversionRequest = _reflection.GeneratedProtocolMessageType('CurrencyConversionRequest', (_message.Message,), {
  'DESCRIPTOR' : _CURRENCYCONVERSIONREQUEST,
  '__module__' : 'demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.CurrencyConversionRequest)
  })
_sym_db.RegisterMessage(CurrencyConversionRequest)

AdRequest = _reflection.GeneratedProtocolMessageType('AdRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADREQUEST,
  '__module__' : 'demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.AdRequest)
  })
_sym_db.RegisterMessage(AdRequest)

AdResponse = _reflection.GeneratedProtocolMessageType('AdResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADRESPONSE,
  '__module__' : 'demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.AdResponse)
  })
_sym_db.RegisterMessage(AdResponse)

Ad = _reflection.GeneratedProtocolMessageType('Ad', (_message.Message,), {
  'DESCRIPTOR' : _AD,
  '__module__' : 'demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.Ad)
  })
_sym_db.RegisterMessage(Ad)



_PRODUCTCATALOGSERVICE = _descriptor.ServiceDescriptor(
  name='ProductCatalogService',
  full_name='hipstershop.ProductCatalogService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=695,
  serialized_end=954,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListProducts',
    full_name='hipstershop.ProductCatalogService.ListProducts',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_LISTPRODUCTSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetProduct',
    full_name='hipstershop.ProductCatalogService.GetProduct',
    index=1,
    containing_service=None,
    input_type=_GETPRODUCTREQUEST,
    output_type=_PRODUCT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SearchProducts',
    full_name='hipstershop.ProductCatalogService.SearchProducts',
    index=2,
    containing_service=None,
    input_type=_SEARCHPRODUCTSREQUEST,
    output_type=_SEARCHPRODUCTSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PRODUCTCATALOGSERVICE)

DESCRIPTOR.services_by_name['ProductCatalogService'] = _PRODUCTCATALOGSERVICE


_CURRENCYSERVICE = _descriptor.ServiceDescriptor(
  name='CurrencyService',
  full_name='hipstershop.CurrencyService',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=957,
  serialized_end=1140,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetSupportedCurrencies',
    full_name='hipstershop.CurrencyService.GetSupportedCurrencies',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_GETSUPPORTEDCURRENCIESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Convert',
    full_name='hipstershop.CurrencyService.Convert',
    index=1,
    containing_service=None,
    input_type=_CURRENCYCONVERSIONREQUEST,
    output_type=_MONEY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CURRENCYSERVICE)

DESCRIPTOR.services_by_name['CurrencyService'] = _CURRENCYSERVICE


_ADSERVICE = _descriptor.ServiceDescriptor(
  name='AdService',
  full_name='hipstershop.AdService',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1142,
  serialized_end=1214,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAds',
    full_name='hipstershop.AdService.GetAds',
    index=0,
    containing_service=None,
    input_type=_ADREQUEST,
    output_type=_ADRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ADSERVICE)

DESCRIPTOR.services_by_name['AdService'] = _ADSERVICE


_ADSERVICEV2 = _descriptor.ServiceDescriptor(
  name='AdServiceV2',
  full_name='hipstershop.AdServiceV2',
  file=DESCRIPTOR,
  index=3,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1216,
  serialized_end=1290,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAds',
    full_name='hipstershop.AdServiceV2.GetAds',
    index=0,
    containing_service=None,
    input_type=_ADREQUEST,
    output_type=_ADRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ADSERVICEV2)

DESCRIPTOR.services_by_name['AdServiceV2'] = _ADSERVICEV2

# @@protoc_insertion_point(module_scope)
