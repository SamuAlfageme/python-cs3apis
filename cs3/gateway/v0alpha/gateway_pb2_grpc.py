# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from cs3.auth.v0alpha import auth_pb2 as cs3_dot_auth_dot_v0alpha_dot_auth__pb2
from cs3.gateway.v0alpha import gateway_pb2 as cs3_dot_gateway_dot_v0alpha_dot_gateway__pb2
from cs3.storageprovider.v0alpha import storageprovider_pb2 as cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2
from cs3.usershareprovider.v0alpha import usershareprovider_pb2 as cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2


class GatewayServiceStub(object):
  """Gateway API

  The Gateway API is the only API exposed direclty to end-clients.
  It is a facade API that all clients should connect to.
  Other APIS like the StorageProviderAPI are internal APIS.

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
    self.GenerateAccessToken = channel.unary_unary(
        '/cs3.gatewayv0alpha.GatewayService/GenerateAccessToken',
        request_serializer=cs3_dot_auth_dot_v0alpha_dot_auth__pb2.GenerateAccessTokenRequest.SerializeToString,
        response_deserializer=cs3_dot_auth_dot_v0alpha_dot_auth__pb2.GenerateAccessTokenResponse.FromString,
        )
    self.WhoAmI = channel.unary_unary(
        '/cs3.gatewayv0alpha.GatewayService/WhoAmI',
        request_serializer=cs3_dot_auth_dot_v0alpha_dot_auth__pb2.WhoAmIRequest.SerializeToString,
        response_deserializer=cs3_dot_auth_dot_v0alpha_dot_auth__pb2.WhoAmIResponse.FromString,
        )
    self.CreateContainer = channel.unary_unary(
        '/cs3.gatewayv0alpha.GatewayService/CreateContainer',
        request_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.CreateContainerRequest.SerializeToString,
        response_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.CreateContainerResponse.FromString,
        )
    self.Delete = channel.unary_unary(
        '/cs3.gatewayv0alpha.GatewayService/Delete',
        request_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.DeleteRequest.SerializeToString,
        response_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.DeleteResponse.FromString,
        )
    self.GetPath = channel.unary_unary(
        '/cs3.gatewayv0alpha.GatewayService/GetPath',
        request_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.GetPathRequest.SerializeToString,
        response_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.GetPathResponse.FromString,
        )
    self.GetQuota = channel.unary_unary(
        '/cs3.gatewayv0alpha.GatewayService/GetQuota',
        request_serializer=cs3_dot_gateway_dot_v0alpha_dot_gateway__pb2.GetQuotaRequest.SerializeToString,
        response_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.GetQuotaResponse.FromString,
        )
    self.InitiateFileDownload = channel.unary_unary(
        '/cs3.gatewayv0alpha.GatewayService/InitiateFileDownload',
        request_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.InitiateFileDownloadRequest.SerializeToString,
        response_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.InitiateFileDownloadResponse.FromString,
        )
    self.InitiateFileUpload = channel.unary_unary(
        '/cs3.gatewayv0alpha.GatewayService/InitiateFileUpload',
        request_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.InitiateFileUploadRequest.SerializeToString,
        response_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.InitiateFileUploadResponse.FromString,
        )
    self.ListContainerStream = channel.unary_stream(
        '/cs3.gatewayv0alpha.GatewayService/ListContainerStream',
        request_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.ListContainerStreamRequest.SerializeToString,
        response_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.ListContainerStreamResponse.FromString,
        )
    self.ListContainer = channel.unary_unary(
        '/cs3.gatewayv0alpha.GatewayService/ListContainer',
        request_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.ListContainerRequest.SerializeToString,
        response_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.ListContainerResponse.FromString,
        )
    self.ListFileVersions = channel.unary_unary(
        '/cs3.gatewayv0alpha.GatewayService/ListFileVersions',
        request_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.ListFileVersionsRequest.SerializeToString,
        response_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.ListFileVersionsResponse.FromString,
        )
    self.ListRecycleStream = channel.unary_stream(
        '/cs3.gatewayv0alpha.GatewayService/ListRecycleStream',
        request_serializer=cs3_dot_gateway_dot_v0alpha_dot_gateway__pb2.ListRecycleStreamRequest.SerializeToString,
        response_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.ListRecycleStreamResponse.FromString,
        )
    self.ListRecycle = channel.unary_unary(
        '/cs3.gatewayv0alpha.GatewayService/ListRecycle',
        request_serializer=cs3_dot_gateway_dot_v0alpha_dot_gateway__pb2.ListRecycleRequest.SerializeToString,
        response_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.ListRecycleResponse.FromString,
        )
    self.Move = channel.unary_unary(
        '/cs3.gatewayv0alpha.GatewayService/Move',
        request_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.MoveRequest.SerializeToString,
        response_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.MoveResponse.FromString,
        )
    self.PurgeRecycle = channel.unary_unary(
        '/cs3.gatewayv0alpha.GatewayService/PurgeRecycle',
        request_serializer=cs3_dot_gateway_dot_v0alpha_dot_gateway__pb2.PurgeRecycleRequest.SerializeToString,
        response_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.PurgeRecycleResponse.FromString,
        )
    self.RestoreFileVersion = channel.unary_unary(
        '/cs3.gatewayv0alpha.GatewayService/RestoreFileVersion',
        request_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.RestoreFileVersionRequest.SerializeToString,
        response_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.RestoreFileVersionResponse.FromString,
        )
    self.RestoreRecycleItem = channel.unary_unary(
        '/cs3.gatewayv0alpha.GatewayService/RestoreRecycleItem',
        request_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.RestoreRecycleItemRequest.SerializeToString,
        response_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.RestoreRecycleItemResponse.FromString,
        )
    self.Stat = channel.unary_unary(
        '/cs3.gatewayv0alpha.GatewayService/Stat',
        request_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.StatRequest.SerializeToString,
        response_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.StatResponse.FromString,
        )
    self.CreateShare = channel.unary_unary(
        '/cs3.gatewayv0alpha.GatewayService/CreateShare',
        request_serializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.CreateShareRequest.SerializeToString,
        response_deserializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.CreateShareResponse.FromString,
        )
    self.RemoveShare = channel.unary_unary(
        '/cs3.gatewayv0alpha.GatewayService/RemoveShare',
        request_serializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.RemoveShareRequest.SerializeToString,
        response_deserializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.RemoveShareResponse.FromString,
        )
    self.GetShare = channel.unary_unary(
        '/cs3.gatewayv0alpha.GatewayService/GetShare',
        request_serializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.GetShareRequest.SerializeToString,
        response_deserializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.GetShareResponse.FromString,
        )
    self.ListShares = channel.unary_unary(
        '/cs3.gatewayv0alpha.GatewayService/ListShares',
        request_serializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.ListSharesRequest.SerializeToString,
        response_deserializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.ListSharesResponse.FromString,
        )
    self.UpdateShare = channel.unary_unary(
        '/cs3.gatewayv0alpha.GatewayService/UpdateShare',
        request_serializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.UpdateShareRequest.SerializeToString,
        response_deserializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.UpdateShareResponse.FromString,
        )
    self.ListReceivedShares = channel.unary_unary(
        '/cs3.gatewayv0alpha.GatewayService/ListReceivedShares',
        request_serializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.ListReceivedSharesRequest.SerializeToString,
        response_deserializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.ListReceivedSharesResponse.FromString,
        )
    self.UpdateReceivedShare = channel.unary_unary(
        '/cs3.gatewayv0alpha.GatewayService/UpdateReceivedShare',
        request_serializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.UpdateReceivedShareRequest.SerializeToString,
        response_deserializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.UpdateReceivedShareResponse.FromString,
        )
    self.GetReceivedShare = channel.unary_unary(
        '/cs3.gatewayv0alpha.GatewayService/GetReceivedShare',
        request_serializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.GetReceivedShareRequest.SerializeToString,
        response_deserializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.GetReceivedShareResponse.FromString,
        )


class GatewayServiceServicer(object):
  """Gateway API

  The Gateway API is the only API exposed direclty to end-clients.
  It is a facade API that all clients should connect to.
  Other APIS like the StorageProviderAPI are internal APIS.

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

  def GenerateAccessToken(self, request, context):
    """*****************************************************************/
    ************************ AUTH ******** **************************/
    *****************************************************************/
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WhoAmI(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateContainer(self, request, context):
    """*****************************************************************/
    ************************ STORAGE PROVIDER ***********************/
    *****************************************************************/
    Creates a new resource of type container.
    MUST return CODE_PRECONDITION_FAILED if the container
    cannot be created at the specified reference.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    """Deletes a resource.
    If a resource specifies the non-empty container (directory, ...),
    then the entire directory is deleted recursively.
    If a resource specifies a reference or symlink type, only the reference is removed (not the target).
    MUST return CODE_NOT_FOUND if the reference does not exist.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPath(self, request, context):
    """Returns the path reference for
    the provided resource id reference.
    MUST return CODE_NOT_FOUND if the reference does not exist
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetQuota(self, request, context):
    """Returns the quota available under the provided
    reference.
    MUST return CODE_NOT_FOUND if the reference does not exist
    MUST return CODE_RESOURCE_EXHAUSTED on exceeded quota limits.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InitiateFileDownload(self, request, context):
    """Initiates the download of a file using an
    out-of-band data transfer mechanism.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InitiateFileUpload(self, request, context):
    """Initiates the upload of a file using an
    out-of-band data transfer mechanism.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListContainerStream(self, request, context):
    """Returns a stream of resource informations
    for the provided reference.
    MUST return CODE_NOT_FOUND if the reference does not exists.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListContainer(self, request, context):
    """Returns a list of resource information
    for the provided reference.
    MUST return CODE_NOT_FOUND if the reference does not exists.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListFileVersions(self, request, context):
    """Returns a list of the versions for a resource of
    type file at the provided reference.
    MUST return CODE_NOT_FOUND if the reference does not exist.
    MUST return CODE_OK and MUST return an empty list if no versions are available.
    TODO: What code if resource not of type file?
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListRecycleStream(self, request, context):
    """Returns a stream of recycle items for this storage provider.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListRecycle(self, request, context):
    """Returns a list of recycle items for this storage provider.
    MUST return CODE_OK and MUST return an empty list if no recycle items are available.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Move(self, request, context):
    """Moves a resource from one reference to another.
    MUST return CODE_NOT_FOUND if any of the references do not exist.
    MUST return CODE_PRECONDITION_FAILED if the source reference
    cannot be moved to the destination reference.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PurgeRecycle(self, request, context):
    """Permanently removes a recycle item from the recycle.
    This operation is irrevocable.
    MUST return CODE_NOT_FOUND if the recycle item id does not exist.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RestoreFileVersion(self, request, context):
    """Restores a file version for the provided reference.
    MUST return CODE_NOT_FOUND if the reference does not exist.
    MUST return CODE_NOT_FOUND if the version does not exist.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RestoreRecycleItem(self, request, context):
    """Restores a recycle item from the recycle.
    MUST return CODE_NOT_FOUND if the recycle item id does not exist.
    MUST return CODE_PRECONDITION_FAILED if the restore_path is non-empty
    and the recycle item cannot be restored to the restore_path.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Stat(self, request, context):
    """Returns the resource information at the provided reference.
    MUST return CODE_NOT_FOUND if the reference does not exist.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateShare(self, request, context):
    """*****************************************************************/
    ************************ USER SHARE PROVIDER ********************/
    *****************************************************************/
    Creates a new share.
    MUST return CODE_NOT_FOUND if the resource reference does not exist.
    MUST return CODE_ALREADY_EXISTS if the share already exists for the 4-tuple consisting of
    (owner, shared_resource, grantee).
    New shares MUST be created in the state SHARE_STATE_PENDING.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveShare(self, request, context):
    """Removes a share.
    MUST return CODE_NOT_FOUND if the share reference does not exist.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetShare(self, request, context):
    """Gets share information for a single share.
    MUST return CODE_NOT_FOUND if the share reference does not exist.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListShares(self, request, context):
    """List the shares the authenticated principal has created,
    both as owner and creator. If a filter is specified, only
    shares satisfying the filter MUST be returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateShare(self, request, context):
    """Updates a share.
    MUST return CODE_NOT_FOUND if the share reference does not exist.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListReceivedShares(self, request, context):
    """List all shares the authenticated principal has received.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateReceivedShare(self, request, context):
    """Update the received share to change the share state or the display name.
    MUST return CODE_NOT_FOUND if the share reference does not exist.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetReceivedShare(self, request, context):
    """Get the information for the given received share reference.
    MUST return CODE_NOT_FOUND if the received share reference does not exist.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GatewayServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GenerateAccessToken': grpc.unary_unary_rpc_method_handler(
          servicer.GenerateAccessToken,
          request_deserializer=cs3_dot_auth_dot_v0alpha_dot_auth__pb2.GenerateAccessTokenRequest.FromString,
          response_serializer=cs3_dot_auth_dot_v0alpha_dot_auth__pb2.GenerateAccessTokenResponse.SerializeToString,
      ),
      'WhoAmI': grpc.unary_unary_rpc_method_handler(
          servicer.WhoAmI,
          request_deserializer=cs3_dot_auth_dot_v0alpha_dot_auth__pb2.WhoAmIRequest.FromString,
          response_serializer=cs3_dot_auth_dot_v0alpha_dot_auth__pb2.WhoAmIResponse.SerializeToString,
      ),
      'CreateContainer': grpc.unary_unary_rpc_method_handler(
          servicer.CreateContainer,
          request_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.CreateContainerRequest.FromString,
          response_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.CreateContainerResponse.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.DeleteRequest.FromString,
          response_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.DeleteResponse.SerializeToString,
      ),
      'GetPath': grpc.unary_unary_rpc_method_handler(
          servicer.GetPath,
          request_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.GetPathRequest.FromString,
          response_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.GetPathResponse.SerializeToString,
      ),
      'GetQuota': grpc.unary_unary_rpc_method_handler(
          servicer.GetQuota,
          request_deserializer=cs3_dot_gateway_dot_v0alpha_dot_gateway__pb2.GetQuotaRequest.FromString,
          response_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.GetQuotaResponse.SerializeToString,
      ),
      'InitiateFileDownload': grpc.unary_unary_rpc_method_handler(
          servicer.InitiateFileDownload,
          request_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.InitiateFileDownloadRequest.FromString,
          response_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.InitiateFileDownloadResponse.SerializeToString,
      ),
      'InitiateFileUpload': grpc.unary_unary_rpc_method_handler(
          servicer.InitiateFileUpload,
          request_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.InitiateFileUploadRequest.FromString,
          response_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.InitiateFileUploadResponse.SerializeToString,
      ),
      'ListContainerStream': grpc.unary_stream_rpc_method_handler(
          servicer.ListContainerStream,
          request_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.ListContainerStreamRequest.FromString,
          response_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.ListContainerStreamResponse.SerializeToString,
      ),
      'ListContainer': grpc.unary_unary_rpc_method_handler(
          servicer.ListContainer,
          request_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.ListContainerRequest.FromString,
          response_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.ListContainerResponse.SerializeToString,
      ),
      'ListFileVersions': grpc.unary_unary_rpc_method_handler(
          servicer.ListFileVersions,
          request_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.ListFileVersionsRequest.FromString,
          response_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.ListFileVersionsResponse.SerializeToString,
      ),
      'ListRecycleStream': grpc.unary_stream_rpc_method_handler(
          servicer.ListRecycleStream,
          request_deserializer=cs3_dot_gateway_dot_v0alpha_dot_gateway__pb2.ListRecycleStreamRequest.FromString,
          response_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.ListRecycleStreamResponse.SerializeToString,
      ),
      'ListRecycle': grpc.unary_unary_rpc_method_handler(
          servicer.ListRecycle,
          request_deserializer=cs3_dot_gateway_dot_v0alpha_dot_gateway__pb2.ListRecycleRequest.FromString,
          response_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.ListRecycleResponse.SerializeToString,
      ),
      'Move': grpc.unary_unary_rpc_method_handler(
          servicer.Move,
          request_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.MoveRequest.FromString,
          response_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.MoveResponse.SerializeToString,
      ),
      'PurgeRecycle': grpc.unary_unary_rpc_method_handler(
          servicer.PurgeRecycle,
          request_deserializer=cs3_dot_gateway_dot_v0alpha_dot_gateway__pb2.PurgeRecycleRequest.FromString,
          response_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.PurgeRecycleResponse.SerializeToString,
      ),
      'RestoreFileVersion': grpc.unary_unary_rpc_method_handler(
          servicer.RestoreFileVersion,
          request_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.RestoreFileVersionRequest.FromString,
          response_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.RestoreFileVersionResponse.SerializeToString,
      ),
      'RestoreRecycleItem': grpc.unary_unary_rpc_method_handler(
          servicer.RestoreRecycleItem,
          request_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.RestoreRecycleItemRequest.FromString,
          response_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.RestoreRecycleItemResponse.SerializeToString,
      ),
      'Stat': grpc.unary_unary_rpc_method_handler(
          servicer.Stat,
          request_deserializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.StatRequest.FromString,
          response_serializer=cs3_dot_storageprovider_dot_v0alpha_dot_storageprovider__pb2.StatResponse.SerializeToString,
      ),
      'CreateShare': grpc.unary_unary_rpc_method_handler(
          servicer.CreateShare,
          request_deserializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.CreateShareRequest.FromString,
          response_serializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.CreateShareResponse.SerializeToString,
      ),
      'RemoveShare': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveShare,
          request_deserializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.RemoveShareRequest.FromString,
          response_serializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.RemoveShareResponse.SerializeToString,
      ),
      'GetShare': grpc.unary_unary_rpc_method_handler(
          servicer.GetShare,
          request_deserializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.GetShareRequest.FromString,
          response_serializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.GetShareResponse.SerializeToString,
      ),
      'ListShares': grpc.unary_unary_rpc_method_handler(
          servicer.ListShares,
          request_deserializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.ListSharesRequest.FromString,
          response_serializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.ListSharesResponse.SerializeToString,
      ),
      'UpdateShare': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateShare,
          request_deserializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.UpdateShareRequest.FromString,
          response_serializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.UpdateShareResponse.SerializeToString,
      ),
      'ListReceivedShares': grpc.unary_unary_rpc_method_handler(
          servicer.ListReceivedShares,
          request_deserializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.ListReceivedSharesRequest.FromString,
          response_serializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.ListReceivedSharesResponse.SerializeToString,
      ),
      'UpdateReceivedShare': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateReceivedShare,
          request_deserializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.UpdateReceivedShareRequest.FromString,
          response_serializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.UpdateReceivedShareResponse.SerializeToString,
      ),
      'GetReceivedShare': grpc.unary_unary_rpc_method_handler(
          servicer.GetReceivedShare,
          request_deserializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.GetReceivedShareRequest.FromString,
          response_serializer=cs3_dot_usershareprovider_dot_v0alpha_dot_usershareprovider__pb2.GetReceivedShareResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'cs3.gatewayv0alpha.GatewayService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
