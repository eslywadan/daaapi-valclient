from concurrent import futures
from threading import Thread
from urllib import response
from tools.account import get_client_info
import grpc
import grpc_cust.clientapival_pb2 as clientapival_pb2
import grpc_cust.clientapival_pb2_grpc as clientapival_pb2_grpc
from tools.config_loader import ConfigLoader


__all__ = 'ClientApiVal'

clientapival_server = ConfigLoader.config("grpc")["clientapival"]["server"]
clientapival_port = ConfigLoader.config("grpc")["clientapival"]["port"]

SERVER_ADDRESS = "%s:%s" %(clientapival_server,clientapival_port)

class ClientAPIValServicer(clientapival_pb2_grpc.ClientAPIValServicer):

    def clientinfo(self, request, context):
      print("Request Client Info called by client(%s)" %(request.clientid))
      info = get_client_info(request.clientid)
      if(info["CLIENT_ID"]!={}):
          print("client id %s has registered info" %(request.clientid))
          response = clientapival_pb2.ClientInfo(
            clientid=request.clientid,
            password = str(info["PASSWORD"][0]),
            type = info["TYPE"][0],
            expiry = str(info["EXPIRY"][0]),
            permission = str(info["PERMISSION"][0])
          )
      else:
          print("client id %s has NO registered info" %(request.clientid))
          response = clientapival_pb2.ClientInfo(
            client_id=request.clientid,
            password = "",
            type = 0,
            expiry = "1900-01-01",
            permission = "None")

      return response


def main():
    server = grpc.server(futures.ThreadPoolExecutor())

    clientapival_pb2_grpc.add_ClientAPIValServicer_to_server(ClientAPIValServicer(),server)

    server.add_insecure_port(SERVER_ADDRESS)
    print("---------------Start Python Client Auth Server----------------------------------")
    server.start()
    print("ClientAPIValServicer.clientinfo listen on server(%s)" %(SERVER_ADDRESS))
    server.wait_for_termination()


if __name__ == '__main__':
  main()