# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from stubs import dbaccess_pb2 as dbaccess__pb2


class DBAccessStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.writeIpAddress = channel.unary_unary(
                '/DBAccess/writeIpAddress',
                request_serializer=dbaccess__pb2.objIpAddress.SerializeToString,
                response_deserializer=dbaccess__pb2.writeResponse.FromString,
                )


class DBAccessServicer(object):
    """Missing associated documentation comment in .proto file."""

    def writeIpAddress(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DBAccessServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'writeIpAddress': grpc.unary_unary_rpc_method_handler(
                    servicer.writeIpAddress,
                    request_deserializer=dbaccess__pb2.objIpAddress.FromString,
                    response_serializer=dbaccess__pb2.writeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DBAccess', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DBAccess(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def writeIpAddress(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DBAccess/writeIpAddress',
            dbaccess__pb2.objIpAddress.SerializeToString,
            dbaccess__pb2.writeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)