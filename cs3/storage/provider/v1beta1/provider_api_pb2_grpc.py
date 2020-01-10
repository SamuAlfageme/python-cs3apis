# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from cs3.storage.provider.v1beta1 import provider_api_pb2 as cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2


class ProviderAPIStub(object):
  """Storage Provider API

  The Storage Provider API is meant to manipulate storage
  resources in the underlying storage system behind the service.

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
    self.AddGrant = channel.unary_unary(
        '/cs3.storage.provider.v1beta1.ProviderAPI/AddGrant',
        request_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.AddGrantRequest.SerializeToString,
        response_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.AddGrantResponse.FromString,
        )
    self.CreateContainer = channel.unary_unary(
        '/cs3.storage.provider.v1beta1.ProviderAPI/CreateContainer',
        request_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.CreateContainerRequest.SerializeToString,
        response_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.CreateContainerResponse.FromString,
        )
    self.Delete = channel.unary_unary(
        '/cs3.storage.provider.v1beta1.ProviderAPI/Delete',
        request_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.DeleteRequest.SerializeToString,
        response_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.DeleteResponse.FromString,
        )
    self.GetPath = channel.unary_unary(
        '/cs3.storage.provider.v1beta1.ProviderAPI/GetPath',
        request_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.GetPathRequest.SerializeToString,
        response_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.GetPathResponse.FromString,
        )
    self.GetQuota = channel.unary_unary(
        '/cs3.storage.provider.v1beta1.ProviderAPI/GetQuota',
        request_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.GetQuotaRequest.SerializeToString,
        response_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.GetQuotaResponse.FromString,
        )
    self.InitiateFileDownload = channel.unary_unary(
        '/cs3.storage.provider.v1beta1.ProviderAPI/InitiateFileDownload',
        request_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.InitiateFileDownloadRequest.SerializeToString,
        response_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.InitiateFileDownloadResponse.FromString,
        )
    self.InitiateFileUpload = channel.unary_unary(
        '/cs3.storage.provider.v1beta1.ProviderAPI/InitiateFileUpload',
        request_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.InitiateFileUploadRequest.SerializeToString,
        response_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.InitiateFileUploadResponse.FromString,
        )
    self.ListGrants = channel.unary_unary(
        '/cs3.storage.provider.v1beta1.ProviderAPI/ListGrants',
        request_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.ListGrantsRequest.SerializeToString,
        response_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.ListGrantsResponse.FromString,
        )
    self.ListContainerStream = channel.unary_stream(
        '/cs3.storage.provider.v1beta1.ProviderAPI/ListContainerStream',
        request_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.ListContainerStreamRequest.SerializeToString,
        response_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.ListContainerStreamResponse.FromString,
        )
    self.ListContainer = channel.unary_unary(
        '/cs3.storage.provider.v1beta1.ProviderAPI/ListContainer',
        request_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.ListContainerRequest.SerializeToString,
        response_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.ListContainerResponse.FromString,
        )
    self.ListFileVersions = channel.unary_unary(
        '/cs3.storage.provider.v1beta1.ProviderAPI/ListFileVersions',
        request_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.ListFileVersionsRequest.SerializeToString,
        response_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.ListFileVersionsResponse.FromString,
        )
    self.ListRecycleStream = channel.unary_stream(
        '/cs3.storage.provider.v1beta1.ProviderAPI/ListRecycleStream',
        request_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.ListRecycleStreamRequest.SerializeToString,
        response_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.ListRecycleStreamResponse.FromString,
        )
    self.ListRecycle = channel.unary_unary(
        '/cs3.storage.provider.v1beta1.ProviderAPI/ListRecycle',
        request_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.ListRecycleRequest.SerializeToString,
        response_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.ListRecycleResponse.FromString,
        )
    self.Move = channel.unary_unary(
        '/cs3.storage.provider.v1beta1.ProviderAPI/Move',
        request_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.MoveRequest.SerializeToString,
        response_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.MoveResponse.FromString,
        )
    self.RemoveGrant = channel.unary_unary(
        '/cs3.storage.provider.v1beta1.ProviderAPI/RemoveGrant',
        request_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.RemoveGrantRequest.SerializeToString,
        response_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.RemoveGrantResponse.FromString,
        )
    self.PurgeRecycle = channel.unary_unary(
        '/cs3.storage.provider.v1beta1.ProviderAPI/PurgeRecycle',
        request_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.PurgeRecycleRequest.SerializeToString,
        response_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.PurgeRecycleResponse.FromString,
        )
    self.RestoreFileVersion = channel.unary_unary(
        '/cs3.storage.provider.v1beta1.ProviderAPI/RestoreFileVersion',
        request_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.RestoreFileVersionRequest.SerializeToString,
        response_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.RestoreFileVersionResponse.FromString,
        )
    self.RestoreRecycleItem = channel.unary_unary(
        '/cs3.storage.provider.v1beta1.ProviderAPI/RestoreRecycleItem',
        request_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.RestoreRecycleItemRequest.SerializeToString,
        response_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.RestoreRecycleItemResponse.FromString,
        )
    self.Stat = channel.unary_unary(
        '/cs3.storage.provider.v1beta1.ProviderAPI/Stat',
        request_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.StatRequest.SerializeToString,
        response_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.StatResponse.FromString,
        )
    self.UpdateGrant = channel.unary_unary(
        '/cs3.storage.provider.v1beta1.ProviderAPI/UpdateGrant',
        request_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.UpdateGrantRequest.SerializeToString,
        response_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.UpdateGrantResponse.FromString,
        )
    self.CreateReference = channel.unary_unary(
        '/cs3.storage.provider.v1beta1.ProviderAPI/CreateReference',
        request_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.CreateReferenceRequest.SerializeToString,
        response_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.CreateReferenceResponse.FromString,
        )
    self.SetArbitraryMetadata = channel.unary_unary(
        '/cs3.storage.provider.v1beta1.ProviderAPI/SetArbitraryMetadata',
        request_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.SetArbitraryMetadataRequest.SerializeToString,
        response_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.SetArbitraryMetadataResponse.FromString,
        )
    self.UnsetArbitraryMetadata = channel.unary_unary(
        '/cs3.storage.provider.v1beta1.ProviderAPI/UnsetArbitraryMetadata',
        request_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.UnsetArbitraryMetadataRequest.SerializeToString,
        response_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.UnsetArbitraryMetadataResponse.FromString,
        )


class ProviderAPIServicer(object):
  """Storage Provider API

  The Storage Provider API is meant to manipulate storage
  resources in the underlying storage system behind the service.

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

  def AddGrant(self, request, context):
    """Adds a new grant for the provided reference.
    MUST return CODE_NOT_FOUND if the reference does not exist
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateContainer(self, request, context):
    """Creates a new resource of type container.
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

  def ListGrants(self, request, context):
    """Returns the list of grants for the provided reference.
    MUST return CODE_NOT_FOUND if the reference does not exists.
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

  def RemoveGrant(self, request, context):
    """Removes a grant for the provided reference.
    This is recursive and atomic for directories. Does not follow references.
    MUST return CODE_NOT_FOUND if the reference does not exist.
    MUST return CODE_NOT_FOUND if grant does not exist.
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

  def UpdateGrant(self, request, context):
    """Updates an ACL for the provided reference.
    MUST return CODE_NOT_FOUND if the reference does not exist.
    MUST return CODE_PRECONDITION_FAILED if the acl does not exist.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateReference(self, request, context):
    """Creates a reference to another resource in the same cluster or another domain (OCM shares).
    The references resource can be accessed by the protocol specificied in the request message.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetArbitraryMetadata(self, request, context):
    """Sets arbitrary metadata into a storage resource.
    Arbitrary metadata is returned in a cs3.storageprovider.v1beta1.ResourceInfo.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UnsetArbitraryMetadata(self, request, context):
    """Unsets arbitrary metdata into a storage resource.
    Arbitrary metadata is returned in a cs3.storageprovider.v1beta1.ResourceInfo.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ProviderAPIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'AddGrant': grpc.unary_unary_rpc_method_handler(
          servicer.AddGrant,
          request_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.AddGrantRequest.FromString,
          response_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.AddGrantResponse.SerializeToString,
      ),
      'CreateContainer': grpc.unary_unary_rpc_method_handler(
          servicer.CreateContainer,
          request_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.CreateContainerRequest.FromString,
          response_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.CreateContainerResponse.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.DeleteRequest.FromString,
          response_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.DeleteResponse.SerializeToString,
      ),
      'GetPath': grpc.unary_unary_rpc_method_handler(
          servicer.GetPath,
          request_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.GetPathRequest.FromString,
          response_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.GetPathResponse.SerializeToString,
      ),
      'GetQuota': grpc.unary_unary_rpc_method_handler(
          servicer.GetQuota,
          request_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.GetQuotaRequest.FromString,
          response_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.GetQuotaResponse.SerializeToString,
      ),
      'InitiateFileDownload': grpc.unary_unary_rpc_method_handler(
          servicer.InitiateFileDownload,
          request_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.InitiateFileDownloadRequest.FromString,
          response_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.InitiateFileDownloadResponse.SerializeToString,
      ),
      'InitiateFileUpload': grpc.unary_unary_rpc_method_handler(
          servicer.InitiateFileUpload,
          request_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.InitiateFileUploadRequest.FromString,
          response_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.InitiateFileUploadResponse.SerializeToString,
      ),
      'ListGrants': grpc.unary_unary_rpc_method_handler(
          servicer.ListGrants,
          request_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.ListGrantsRequest.FromString,
          response_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.ListGrantsResponse.SerializeToString,
      ),
      'ListContainerStream': grpc.unary_stream_rpc_method_handler(
          servicer.ListContainerStream,
          request_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.ListContainerStreamRequest.FromString,
          response_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.ListContainerStreamResponse.SerializeToString,
      ),
      'ListContainer': grpc.unary_unary_rpc_method_handler(
          servicer.ListContainer,
          request_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.ListContainerRequest.FromString,
          response_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.ListContainerResponse.SerializeToString,
      ),
      'ListFileVersions': grpc.unary_unary_rpc_method_handler(
          servicer.ListFileVersions,
          request_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.ListFileVersionsRequest.FromString,
          response_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.ListFileVersionsResponse.SerializeToString,
      ),
      'ListRecycleStream': grpc.unary_stream_rpc_method_handler(
          servicer.ListRecycleStream,
          request_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.ListRecycleStreamRequest.FromString,
          response_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.ListRecycleStreamResponse.SerializeToString,
      ),
      'ListRecycle': grpc.unary_unary_rpc_method_handler(
          servicer.ListRecycle,
          request_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.ListRecycleRequest.FromString,
          response_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.ListRecycleResponse.SerializeToString,
      ),
      'Move': grpc.unary_unary_rpc_method_handler(
          servicer.Move,
          request_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.MoveRequest.FromString,
          response_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.MoveResponse.SerializeToString,
      ),
      'RemoveGrant': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveGrant,
          request_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.RemoveGrantRequest.FromString,
          response_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.RemoveGrantResponse.SerializeToString,
      ),
      'PurgeRecycle': grpc.unary_unary_rpc_method_handler(
          servicer.PurgeRecycle,
          request_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.PurgeRecycleRequest.FromString,
          response_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.PurgeRecycleResponse.SerializeToString,
      ),
      'RestoreFileVersion': grpc.unary_unary_rpc_method_handler(
          servicer.RestoreFileVersion,
          request_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.RestoreFileVersionRequest.FromString,
          response_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.RestoreFileVersionResponse.SerializeToString,
      ),
      'RestoreRecycleItem': grpc.unary_unary_rpc_method_handler(
          servicer.RestoreRecycleItem,
          request_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.RestoreRecycleItemRequest.FromString,
          response_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.RestoreRecycleItemResponse.SerializeToString,
      ),
      'Stat': grpc.unary_unary_rpc_method_handler(
          servicer.Stat,
          request_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.StatRequest.FromString,
          response_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.StatResponse.SerializeToString,
      ),
      'UpdateGrant': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateGrant,
          request_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.UpdateGrantRequest.FromString,
          response_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.UpdateGrantResponse.SerializeToString,
      ),
      'CreateReference': grpc.unary_unary_rpc_method_handler(
          servicer.CreateReference,
          request_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.CreateReferenceRequest.FromString,
          response_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.CreateReferenceResponse.SerializeToString,
      ),
      'SetArbitraryMetadata': grpc.unary_unary_rpc_method_handler(
          servicer.SetArbitraryMetadata,
          request_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.SetArbitraryMetadataRequest.FromString,
          response_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.SetArbitraryMetadataResponse.SerializeToString,
      ),
      'UnsetArbitraryMetadata': grpc.unary_unary_rpc_method_handler(
          servicer.UnsetArbitraryMetadata,
          request_deserializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.UnsetArbitraryMetadataRequest.FromString,
          response_serializer=cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2.UnsetArbitraryMetadataResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'cs3.storage.provider.v1beta1.ProviderAPI', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))