from clientapival_server import ClientAPIValServicer as svr
import grpc_cust.clientapival_pb2 as clientapival_pb2

svr = svr()

def test_clientinfo():
    request = clientapival_pb2.ClientId(clientid="mfg")
    info = svr.clientinfo(request,context=None)
    assert info.password == "28bfd0031d38c6100a0491cf5b18fa6ef861002d"

def test_clientapikey():
    request = clientapival_pb2.ClientCred(clientid="mfg", password="mfg")
    apikey = svr.clientapikey(request,context=None)
    token = apikey.apikey
    assert token is not None
    verifiedapikey(token)

def verifiedapikey(token):
    request = clientapival_pb2.APIKey(apikey=token)
    verifiedresult = svr.verifiedapikey(request,context=None)
    assert verifiedresult.assertion