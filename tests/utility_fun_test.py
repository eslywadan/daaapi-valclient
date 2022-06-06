from tools.account import *
from tools.logger import Logger

'''The server side tests have two parts: 
the first part is the function test
and the second part is the servicer test'''

class TestClientAPIValFuns():

    def case(self, clientid, password):
      self.clientid = clientid
      self.password = password
      self.obsapikey = "12345"

    def get_client_info(self):
      info = get_client_info(self.clientid)
      print(info)
      self.info = info
      assert self.clientid == info["CLIENT_ID"][0]

    def get_apikey(self):
      response = check_client_id_password(self.clientid, self.password)
      self.apikey = response["apikey"]
      assert self.apikey is not None

    def verified_apikey_pass(self):
      assert check_and_log(self.apikey) == True

    def verified_apikey_fail(self):
      assert check_and_log(self.obsapikey) == False



def test_valclientapi_fun():
  testcase1 = TestClientAPIValFuns()
  testcase1.case("mfg","mfg")
  testcase1.get_client_info()
  testcase1.get_apikey()
  testcase1.verified_apikey_pass()
  testcase1.verified_apikey_fail()
