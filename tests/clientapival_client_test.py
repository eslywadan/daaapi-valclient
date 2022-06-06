from grpc_cust.clientapival_client import get_clientinfo, get_clientapikey, get_verified_apikey
from clientapival_server import GrpcSvr


def test_clientapival_client():
    grpcsvr = GrpcSvr()
    info = get_clientinfo("mfg")
    assert info is not None

    apikey = get_clientapikey("mfg","mfg")
    token = apikey.apikey
    assert token is not None

    apikey = get_clientapikey("mfg","mfg")
    token = apikey.apikey
    verifiedresult = get_verified_apikey(token)
    assert verifiedresult
    
    del grpcsvr


    
