# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from cs3.auth.registry.v1beta1 import registry_api_pb2 as cs3_dot_auth_dot_registry_dot_v1beta1_dot_registry__api__pb2


class RegistryAPIStub(object):
  """Auth Registry API

  The Auth Registry API is meant to as registry to obtain
  information of available auth providers.
  For example, to use OIDC or Kerberos for authentication.

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
    self.GetAuthProvider = channel.unary_unary(
        '/cs3.auth.registry.v1beta1.RegistryAPI/GetAuthProvider',
        request_serializer=cs3_dot_auth_dot_registry_dot_v1beta1_dot_registry__api__pb2.GetAuthProviderRequest.SerializeToString,
        response_deserializer=cs3_dot_auth_dot_registry_dot_v1beta1_dot_registry__api__pb2.GetAuthProviderResponse.FromString,
        )
    self.ListAuthProviders = channel.unary_unary(
        '/cs3.auth.registry.v1beta1.RegistryAPI/ListAuthProviders',
        request_serializer=cs3_dot_auth_dot_registry_dot_v1beta1_dot_registry__api__pb2.ListAuthProvidersRequest.SerializeToString,
        response_deserializer=cs3_dot_auth_dot_registry_dot_v1beta1_dot_registry__api__pb2.ListAuthProvidersResponse.FromString,
        )


class RegistryAPIServicer(object):
  """Auth Registry API

  The Auth Registry API is meant to as registry to obtain
  information of available auth providers.
  For example, to use OIDC or Kerberos for authentication.

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

  def GetAuthProvider(self, request, context):
    """Returns the auth provider that is reponsible for the given
    resource reference.
    MUST return CODE_NOT_FOUND if the reference does not exist.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListAuthProviders(self, request, context):
    """Returns a list of the available auth providers known by this registry.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RegistryAPIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetAuthProvider': grpc.unary_unary_rpc_method_handler(
          servicer.GetAuthProvider,
          request_deserializer=cs3_dot_auth_dot_registry_dot_v1beta1_dot_registry__api__pb2.GetAuthProviderRequest.FromString,
          response_serializer=cs3_dot_auth_dot_registry_dot_v1beta1_dot_registry__api__pb2.GetAuthProviderResponse.SerializeToString,
      ),
      'ListAuthProviders': grpc.unary_unary_rpc_method_handler(
          servicer.ListAuthProviders,
          request_deserializer=cs3_dot_auth_dot_registry_dot_v1beta1_dot_registry__api__pb2.ListAuthProvidersRequest.FromString,
          response_serializer=cs3_dot_auth_dot_registry_dot_v1beta1_dot_registry__api__pb2.ListAuthProvidersResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'cs3.auth.registry.v1beta1.RegistryAPI', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
