from grpc_cust.clientapival_client import get_clientinfo, get_clientapikey, get_verified_apikey
from clientapival_server import TmpValClientSvr

rpc_svr = TmpValClientSvr()

def test_get_clientinfo():
    info = get_clientinfo("mfg")
    print(info)
    assert info is not None

def test_get_clientapikey():
    apikey = get_clientapikey("mfg","mfg")
    token = apikey.apikey
    assert token is not None

def test_verified_apikey():
    apikey = get_clientapikey("mfg","mfg")
    token = apikey.apikey
    verifiedresult = get_verified_apikey(token)
    assert verifiedresult


    
