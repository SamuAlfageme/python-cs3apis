# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from cs3.app.provider.v1beta1 import provider_api_pb2 as cs3_dot_app_dot_provider_dot_v1beta1_dot_provider__api__pb2


class ProviderAPIStub(object):
  """import "cs3/appprovider/v1beta1/resources.proto";

  App Provider API

  The App Provider API is responsible for creating urls that
  will render a viewer or editor for the given resource.
  For example, an OnlyOffice or HackMD editor.

  The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL
  NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and
  "OPTIONAL" in this document are to be interpreted as described in
  RFC 2119.

  The following are global requirements that apply to all methods:
  Any method MUST return CODE_OK on a succesful operation.
  Any method MAY return NOT_IMPLEMENTED.
  Any method MAY return INTERNAL.
  Any method MAY return UNKNOWN.
  Any method MAY return UNAUTHENTICATED.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Open = channel.unary_unary(
        '/cs3.app.provider.v1beta1.ProviderAPI/Open',
        request_serializer=cs3_dot_app_dot_provider_dot_v1beta1_dot_provider__api__pb2.OpenRequest.SerializeToString,
        response_deserializer=cs3_dot_app_dot_provider_dot_v1beta1_dot_provider__api__pb2.OpenResponse.FromString,
        )


class ProviderAPIServicer(object):
  """import "cs3/appprovider/v1beta1/resources.proto";

  App Provider API

  The App Provider API is responsible for creating urls that
  will render a viewer or editor for the given resource.
  For example, an OnlyOffice or HackMD editor.

  The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL
  NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and
  "OPTIONAL" in this document are to be interpreted as described in
  RFC 2119.

  The following are global requirements that apply to all methods:
  Any method MUST return CODE_OK on a succesful operation.
  Any method MAY return NOT_IMPLEMENTED.
  Any method MAY return INTERNAL.
  Any method MAY return UNKNOWN.
  Any method MAY return UNAUTHENTICATED.
  """

  def Open(self, request, context):
    """Returns the iframe url
    MUST return CODE_NOT_FOUND if the resource does not exist.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ProviderAPIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Open': grpc.unary_unary_rpc_method_handler(
          servicer.Open,
          request_deserializer=cs3_dot_app_dot_provider_dot_v1beta1_dot_provider__api__pb2.OpenRequest.FromString,
          response_serializer=cs3_dot_app_dot_provider_dot_v1beta1_dot_provider__api__pb2.OpenResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'cs3.app.provider.v1beta1.ProviderAPI', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
