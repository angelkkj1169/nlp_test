# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from models import nlp_server_pb2 as nlp__server__pb2

class NLPServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getNlc = channel.unary_unary(
                '/NLPServer/getNlc',
                request_serializer=nlp__server__pb2.nlcReq.SerializeToString,
                response_deserializer=nlp__server__pb2.nlcRes.FromString,
                )
        self.getModelList = channel.unary_unary(
                '/NLPServer/getModelList',
                request_serializer=nlp__server__pb2.getModelReq.SerializeToString,
                response_deserializer=nlp__server__pb2.getModelRes.FromString,
                )
        self.reqSimulation = channel.unary_unary(
                '/NLPServer/reqSimulation',
                request_serializer=nlp__server__pb2.simulationReq.SerializeToString,
                response_deserializer=nlp__server__pb2.simulationRes.FromString,
                )
        self.getItn = channel.unary_unary(
                '/NLPServer/getItn',
                request_serializer=nlp__server__pb2.itnReq.SerializeToString,
                response_deserializer=nlp__server__pb2.itnRes.FromString,
                )


class NLPServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getNlc(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getModelList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def reqSimulation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getItn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NLPServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getNlc': grpc.unary_unary_rpc_method_handler(
                    servicer.getNlc,
                    request_deserializer=nlp__server__pb2.nlcReq.FromString,
                    response_serializer=nlp__server__pb2.nlcRes.SerializeToString,
            ),
            'getModelList': grpc.unary_unary_rpc_method_handler(
                    servicer.getModelList,
                    request_deserializer=nlp__server__pb2.getModelReq.FromString,
                    response_serializer=nlp__server__pb2.getModelRes.SerializeToString,
            ),
            'reqSimulation': grpc.unary_unary_rpc_method_handler(
                    servicer.reqSimulation,
                    request_deserializer=nlp__server__pb2.simulationReq.FromString,
                    response_serializer=nlp__server__pb2.simulationRes.SerializeToString,
            ),
            'getItn': grpc.unary_unary_rpc_method_handler(
                    servicer.getItn,
                    request_deserializer=nlp__server__pb2.itnReq.FromString,
                    response_serializer=nlp__server__pb2.itnRes.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'NLPServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NLPServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getNlc(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NLPServer/getNlc',
            nlp__server__pb2.nlcReq.SerializeToString,
            nlp__server__pb2.nlcRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getModelList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NLPServer/getModelList',
            nlp__server__pb2.getModelReq.SerializeToString,
            nlp__server__pb2.getModelRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def reqSimulation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NLPServer/reqSimulation',
            nlp__server__pb2.simulationReq.SerializeToString,
            nlp__server__pb2.simulationRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getItn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NLPServer/getItn',
            nlp__server__pb2.itnReq.SerializeToString,
            nlp__server__pb2.itnRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)